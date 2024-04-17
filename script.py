# -*- coding: utf-8 -*-
import naoqi
from naoqi import ALProxy
import paramiko 
import time
import subprocess

IP = '10.1.95.144'
tts = ALProxy("ALTextToSpeech", IP, 9559)
audio_recorder = ALProxy("ALAudioRecorder", IP, 9559)


def record_audio(soundRecordPath, localPath):
    audio_recorder.startMicrophonesRecording(soundRecordPath, "wav", 16000, (0,0,1,0))
    time.sleep(5)
    audio_recorder.stopMicrophonesRecording()

    ssh_client =paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=IP,port=22,username='nao',password='nao')
    ftp_client =ssh_client.open_sftp()
    ftp_client.get(soundRecordPath, localPath)
    ftp_client.close()

    ssh_client.close()

    print("audio recorded")

def run_script(script_path, txt_path):
    
    conda_environment_name = 'test'

    # Activate the Conda environment and run the subprocess
    try:
        subprocess.check_call(['conda', 'run', '-n', conda_environment_name, 'python', script_path])
        print("Subprocess completed successfully.")
    except subprocess.CalledProcessError as e:
        print('error')


    with open(txt_path, 'r') as file:
        lines = file.readlines()
        concatenated_text = ' '.join(lines).replace('\n', '')

    print("Concatenated Text:")
    print(concatenated_text)

    return concatenated_text


if __name__ == "__main__":

    soundRecordPath = "/home/nao/audio.wav"
    localPath = "/home/nadasamir/Desktop/cognitive/audio/audio.wav"

    integrated_script_path = '/home/nadasamir/Desktop/cognitive/integrated_speech_modules.py'
    response_txt_path = '/home/nadasamir/Desktop/cognitive/audio/response.txt' 

    speech2txt_script_path = '/home/nadasamir/Desktop/cognitive/speech2txt.py'
    activation_txt_path = '/home/nadasamir/Desktop/cognitive/audio/activation.txt'  

    sentence = ""
    # activation = "what's up"
    activation = 'صباح الخير'
    # deactivation = "stop chatting"
    deactivation = 'مع السلامه'
    # not_recognized = "Speech could not be recognized"
    not_recognized = "لم أسمعُكَ جيداً"

    # russian = 'Погода сегодня отличная! Как замечательно!'

    # print(russian)

    # tts.say("hello")
    tts.setLanguage('Arabic')
    # tts.say('صباح الفُل')

    # record_audio(soundRecordPath, localPath)
    # print('recorded')
    # response = run_script(integrated_script_path, response_txt_path)
    print('start recording')
    # record_audio(soundRecordPath, localPath)
    # sentence = run_script(speech2txt_script_path, activation_txt_path)
    # tts.say(sentence)
    # tts.say('موزارتْ ، نَغْمَةُ الكَوْنِ المُتَرْجَمَةِ إِلَى لحنٍ فَريدٌ ، في قَلْبِهِ الفَنُّ يَتَجَلَّى ، وَفي روحِهِ يَلْتَقيَ السِّحْرَ والْإِلْهامُ')
    while True:

        while sentence != activation:

            record_audio(soundRecordPath, localPath)
            sentence = run_script(speech2txt_script_path, activation_txt_path)
            if sentence == not_recognized:
                tts.say(not_recognized)   
            # tts.say(sentence) 

        tts.say('مرحباً')
    #     tts.say("hello there")

        while True:

            tts.say("كيف أُساعِدُك؟")
            record_audio(soundRecordPath, localPath)
            sentence = run_script(speech2txt_script_path, activation_txt_path)

            if sentence == not_recognized:
                tts.say(not_recognized)
            else:
                if sentence == deactivation:
                    tts.say("إلى اللقاء")
                    break

            response = run_script(integrated_script_path, response_txt_path)
            print(response)
            tts.say(response)

