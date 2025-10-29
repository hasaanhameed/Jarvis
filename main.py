import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env
load_dotenv()

# Get keys and device index
newsApi = os.getenv("NEWS_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")
MIC_INDEX = int(os.getenv("MIC_INDEX", 0))  # Default to 0 if not set

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    """Process user voice commands."""
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif c.startswith("play"):
        try:
            song = c.split(" ")[1]
            link = musicLibrary.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak("Sorry, I don't have that song.")
        except IndexError:
            speak("Please specify a song name.")

    elif "news" in c:
        if not newsApi:
            speak("News API key not found. Please configure it in your .env file.")
            return
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsApi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
            for article in articles[:5]:
                print(article["title"])
                speak(article["title"])
        else:
            speak("Failed to fetch news.")
            print("HTTP status code:", r.status_code)

    elif any(bye_word in c for bye_word in ["bye", "goodbye", "exit", "quit", "shutdown"]):
        speak("Goodbye! Shutting down Jarvis.")
        sys.exit()

    else:
        output = openAiProcess(c)
        if output:
            speak(output)

def openAiProcess(c):
    """Use OpenAI for general queries."""
    if not openai_key:
        speak("OpenAI key not found. Please configure it in your .env file.")
        return None

    client = OpenAI(api_key=openai_key)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa."},
            {"role": "user", "content": c}
        ]
    )
    response = completion.choices[0].message.content
    print("Jarvis:", response)
    return response


if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()

        try:
            with sr.Microphone(device_index=MIC_INDEX) as source:
                print("Listening...")
                audio = r.listen(source)

            print("Recognizing...")
            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("How can I help you?")
                with sr.Microphone(device_index=MIC_INDEX) as source:
                    print("Jarvis is Active...")
                    audio = r.listen(source)
                    print("Recognizing...")
                    command = r.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            speak("Goodbye!")
            break
