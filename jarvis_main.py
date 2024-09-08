import requests
from bs4 import BeautifulSoup
import pyttsx3
import speech_recognition
import datetime
import os


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")  # list of voices from the engine
engine.setProperty("voice", voices[0].id)  # changing
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = .7
        r.energy_threshold = 500
        audio = r.listen(source, 0, 4)
        try:
            print("Understanding....")
            query = r.recognize_google(audio, language='en')
            print(f"You said : {query}")
        except Exception as e:
            print("Say that again please..")
            return "None"
        return query


def alarm(query):
    timehere = open('Alarmytext.txt', 'a')
    timehere.write(query)
    timehere.close()
    os.startfile('alarm.py')


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'wake up' in query:
            from greet import greetme
            greetme()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir,You can call anytime")
                    break
                elif "hello" in query:
                    speak("Hello sir How are You?")
                elif "i am fine" in query:
                    speak("Thats great")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("Welcome sir")
                elif "open" in query:
                    from dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from dictapp import closeappweb
                    closeappweb(query)
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "YouTube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from search import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search = "temperature in chandigarh"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find('div', class_="BNeawe").text
                    print(f"current{search} is {temp}")
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in chandigarh"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find('div', class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    print(f"Sir, the time is {strTime}")
                    speak(f"Sir, the time is {strTime}")
                elif "jarvis sleep" in query:
                    speak("Going to sleep ,sir")
                    from gui import play_gif
                    play_gif
                    exit()
