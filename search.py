import pyttsx3
import speech_recognition
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshol=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)
        try:
            print("Understanding....")
            query=r.recognize_google(audio,language='en')
            print(f"You said : {query}") 
        except Exception as e:
            print("Say that again please..")  
            return "None"
        return query
    
query=takeCommand().lower()

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices") #list of voices from the engine
engine.setProperty("voice",voices[0].id)#changing
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query=query.replace("google","")
        speak("This is what i found on google")

    try:
        pywhatkit.search(query)
        result=googleScrap.summary(query,1)
        print(result)
        speak(result)
    except:
        speak("No speakable output available")

def searchYoutube(query):
    if "youtube" in query:
        speak("This is what I found on search!")
        query=query.replace("jarvis","")
        query=query.replace("youtube","")
        query=query.replace("youtube search","")
        query=query.replace("search","")
        web="https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done ,Sir")

def searchWikipedia(query):
    if 'wikipedia' in query:
         speak(f"Searching wikipedia.....") #wikipedia
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=4)
         speak("According to Wikipedia")
         print(results)
         speak(results)
        