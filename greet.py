import pyttsx3
import datetime

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices") #list of voices from the engine
engine.setProperty("voice",voices[0].id)#changing
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetme():
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!")
    elif hour>12 and hour<=18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("Please tell me !  How can I help you?")
