# Jarvis - Voice Assistant

Jarvis is a Python-based voice assistant that performs various tasks through voice commands. It can open websites, play music, fetch live news updates, and even respond to general questions using the OpenAI API.

## Features

- Voice command recognition using SpeechRecognition
- Text-to-speech responses using pyttsx3
- Opens common websites (Google, YouTube, LinkedIn)
- Plays music from a predefined library
- Fetches top headlines via NewsAPI
- AI-powered conversational responses using OpenAI GPT
- Graceful shutdown with exit keywords

## Tech Stack

- Python 3.10+
- SpeechRecognition
- pyttsx3
- Requests
- OpenAI API
- NewsAPI
-

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/hasaanhameed/Jarvis.git
cd Jarvis

### 2. Create a virtual environment
python -m venv env
env\Scripts\activate

### 3. Install dependencies
Install all required packages listed in `requirements.txt`:
pip install -r requirements.txt

### 4. Insert API keys
Open main.py and add your API keys in the variables provided:
newsApi = "YOUR_NEWSAPI_KEY"
openaiApi = "YOUR_OPENAI_KEY"

### 5. Check your microphone index
If your microphone doesn’t work, adjust the device_index inside:
with sr.Microphone(device_index=3) as source:

### 6. Run the program
python main.py

When prompted, say "Jarvis" to activate the assistant and then give commands like:
“Open Google”
“Play Invincible”
“Tell me the news”
“Who are you?”
“Exit” or “Shutdown” to close



