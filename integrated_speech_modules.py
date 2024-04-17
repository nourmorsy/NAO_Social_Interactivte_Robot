'''
  Dependencies:
    sentencepiece
    transformers
    openai==0.28
    sacremoses
    torchaudio
    datasets
    IPython
    torch
'''

from transformers import WhisperProcessor, WhisperForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import FSMTForConditionalGeneration, FSMTTokenizer
from transformers import VitsModel, AutoTokenizer
from datasets import load_dataset
from transformers import pipeline
from IPython.display import Audio
import torchaudio
# from torchaudio import save
import openai
import torch
import speech_recognition as sr

from transformers import GPT2TokenizerFast, pipeline
#for base and medium
from transformers import GPT2LMHeadModel
#for large and mega
# pip install arabert
from arabert.aragpt2.grover.modeling_gpt2 import GPT2LMHeadModel

from arabert.preprocess import ArabertPreprocessor

from farasa.diacratizer import FarasaDiacritizer 


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


def sentiment_analysis(transcription):

  sentiment_analysis = pipeline("text-classification", model="siebert/sentiment-roberta-large-english")
  sentiment = sentiment_analysis(transcription)

  return sentiment[0]['label']

def dicat(txt):
  farasa_diacritizer = FarasaDiacritizer()

  # Arabic text without diacritics
  # arabic_text = "اللغة العربية جميلة"

  # Diacritize the Arabic text
  diacritized_text = farasa_diacritizer.diacritize(txt)

  return diacritized_text 

   

def chatGPT(prmpt):

  openai.api_key = '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'
  response = openai.Completion.create(
    engine="text-davinci-003",  # You can choose a different engine
    prompt=prmpt,
    max_tokens=1000
  )

  return response['choices'][0]['text']

def araGPT(prmpt):


  MODEL_NAME='aubmindlab/aragpt2-base'
  arabert_prep = ArabertPreprocessor(model_name=MODEL_NAME)

  text="أهلا بك"
  text_clean = arabert_prep.preprocess(text)

  model = GPT2LMHeadModel.from_pretrained(MODEL_NAME)
  tokenizer = GPT2TokenizerFast.from_pretrained(MODEL_NAME)
  generation_pipeline = pipeline("text-generation",model=model,tokenizer=tokenizer)

  #feel free to try different decoding settings
  generation_pipeline(text,
      pad_token_id=tokenizer.eos_token_id,
      num_beams=10,
      max_length=200,
      top_p=0.9,
      repetition_penalty = 3.0,
      no_repeat_ngram_size = 3)[0]['generated_text']

  # return ''


def trans2russian(english_txt):

  mname = "facebook/wmt19-en-ru"
  tokenizer = FSMTTokenizer.from_pretrained(mname)
  model = FSMTForConditionalGeneration.from_pretrained(mname)

  input_ids = tokenizer.encode(english_txt, return_tensors="pt")
  outputs = model.generate(input_ids)
  translation = tokenizer.decode(outputs[0], skip_special_tokens=True)

  return translation


def txt2speech(audio_path, txt):

  model = VitsModel.from_pretrained("facebook/mms-tts-rus")
  tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-rus")

  inputs = tokenizer(txt, return_tensors="pt")

  with torch.no_grad():
      output = model(**inputs).waveform

  torchaudio.save(audio_path, output, model.config.sampling_rate, format='wav')
  # Audio(audio_path)

def save_file(path, txt):
  with open(path, 'w') as file:
      file.write(txt)

def read_file(txt_path):
  with open(txt_path, 'r') as file:
          lines = file.readlines()
          concatenated_text = ' '.join(lines).replace('\n', '')

  print("Concatenated Text:")
  print(concatenated_text)

  return concatenated_text

if __name__ == '__main__':

  # user_audio_path = '/home/nadasamir/Desktop/cognitive/audio/audio.wav'
  # response_audio_path = '/home/nadasamir/Desktop/cognitive/audio/response.wav'
  response_txt_path = '/home/nadasamir/Desktop/cognitive/audio/response.txt'
  activation_txt_path = '/home/nadasamir/Desktop/cognitive/audio/activation.txt'

  # english_txt = speech2txt(user_audio_path)
  english_txt = read_file(activation_txt_path)

  # english_txt = 'أحضر لى التفاحه من المطبخ'
  

  if english_txt != "" :
    print(english_txt)
    # sentiment = sentiment_analysis(english_txt)
    # print(sentiment)
    # prompt = f"{english_txt} Reply to previous sententce in 2 lines including the emotion of the user is {sentiment}"
    prompt = english_txt + 'تحدث معى فى جملتين'
    print(f'output: {prompt}')
    english_response = chatGPT(prompt)
    print(f'chatgpt: {english_response}')
    correction = dicat(english_response)
    print(f'chatgpt: {correction}')
    # english_response = araGPT(prompt)
    # print(english_response)

  else:
    #  english_response = "Speech could not be recognized"
     english_response = 'لم أسمع جيداً'

  # save_file(response_txt_path, english_response)
  save_file(response_txt_path, correction)

  

  # russian_response = trans2russian(english_response)
  # print(russian_response)
  # txt2speech(response_audio_path, russian_response)
  # print(f'\n\n{prompt}\n{english_response}\n{russian_response}\n')

