# -*- coding: utf-8 -*-

import speech_recognition as sr

def speech2txt(audioPath):
  
    # initialize the recognizer
    r = sr.Recognizer()

    try:
        # open the file
        with sr.AudioFile(audioPath) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_google(audio_data, language='ar')
            print(text)
            print("Text recognized:", text)
    except sr.UnknownValueError:
        print("Speech could not be recognized")
        text = ""

    return text

def save_file(path, txt):
  with open(path, 'w') as file:
      file.write(txt)


user_audio_path = '/home/nadasamir/Desktop/cognitive/audio/audio.wav'
activation_txt_path = '/home/nadasamir/Desktop/cognitive/audio/activation.txt'


english_txt = speech2txt(user_audio_path)

# if english_txt == "" :
#     english_txt = "Speech could not be recognized"

if english_txt == '':
    english_txt = "لم أسمعُكَ جيداً"

save_file(activation_txt_path, english_txt)