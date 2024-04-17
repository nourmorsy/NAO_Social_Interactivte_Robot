

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
            text = r.recognize_google(audio_data)
            print("Text recognized:", text)
    except sr.UnknownValueError:
        print("Speech could not be recognized")
        text = ""

    return text

user_audio_path = '/home/nadasamir/Desktop/cognitive/audio/test_audio.wav'

speech2txt(user_audio_path)