# from transformers import WhisperProcessor, WhisperForConditionalGeneration
import transformers
# import torchaudio
# import torch

# Load model and processor
# processor = WhisperProcessor.from_pretrained("openai/whisper-large-v2")
# model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v2")
# model.config.forced_decoder_ids = None

# # Load audio file
# wav_file_path = "/content/audio_old.wav"
# waveform, sample_rate = torchaudio.load(wav_file_path)

# # Process audio using the Whisper processor
# input_features = processor(waveform.squeeze().numpy(), sampling_rate=sample_rate, return_tensors="pt").input_features

# # Generate token ids
# predicted_ids = model.generate(input_features)
# transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)

# print("Transcription:", transcription[0])