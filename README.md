# NAO Social Interactivte Robot

## Project Goal and Overview

The **NAO_social_interactive_robot** project aims to create a socially interactive robot using advanced cognitive and language processing capabilities. This project brings NAO to life with By leveraging natural language processing and teleoperation capabilities, this robot can engage in meaningful conversations and mirror human gestures, enhancing social interaction.

---

## Robot Used
This project uses **NAO**, a humanoid robot developed by SoftBank Robotics. NAO is designed for interactive applications and is equipped with sensors, microphones, and speakers, enabling it to process speech, understand emotions, and respond in a human-like manner.

---

## Key Features
1. **Sentiment Analysis** - Analyzes the sentiment of recognized speech to gauge user emotion.
2. **Face Emotion Recognition** - Identifies facial expressions to determine user emotions visually.
3. **Voice Recorder** - Captures audio input from users.
4. **Speech Recognition** - Converts recorded speech into text for further processing.
5. **LLM Integration** - Uses a large language model to generate contextually appropriate responses.
6. **Teleoperation** - Allows remote control and monitoring of NAO's movements, with gesture recognition through video feeds.
7. **Text-to-Speech (TTS)** - Enables NAO to vocalize responses.

---

## Installation

### NAOqi SDK Installation

The project requires the NAOqi SDK to communicate with the Pepper robot. Follow these steps to install the NAOqi SDK for Python:

1. Download the NAOqi SDK from [NAOqi SDK](https://www.aldebaran.com/en/support/pepper-naoqi-2-9/python-sdk-255-linux-64).
2. Extract the SDK package in your preferred directory.
3. Add the SDK path to your Python environment:
   ```bash
   export PYTHONPATH=${PYTHONPATH}:/path/to/naoqi/sdk
   ```
---

### Script Descriptions

- **`integrated_speech_modules.py`**  
  Integrates speech recognition, sentiment analysis, and language processing for handling audio input from NAO.

- **`new_integrate.py`**  
  Acts as the main controller, coordinating speech recognition, teleoperation, and TTS functionalities.

- **`script.py`**  
  Initializes NAO’s interactive functions and starts the main interaction loop.

- **`speech2txt.py`**  
  Handles converting NAO's audio input into text for further processing.

- **`test_speech2text.py`**  
  Provides test cases to validate the speech-to-text functionality.

---

### Running the Project

1. Start the main interaction:
   ```bash
   python script.py
   ```

2. Test the speech-to-text functionality:
   ```bash
   python test_speech2text.py
   ```
---

### Acknowledgment

We would like to extend our sincere gratitude to our assistant teacher, [Hossam Ahmed](https://github.com/Hossamvs), for his invaluable support and guidance throughout the development of this project. His expertise, advice, and encouragement were instrumental in helping us bring the **NAO_social_interactive_robot** to life. Thank you for your continuous support and mentorship.
