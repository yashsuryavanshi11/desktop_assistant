import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices") #list of voices from the engine
engine.setProperty("voice",voices[0].id)#changing
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapp={"commandprompt":"cmd","paint":"paint","excel":"excel","chrome":"chrome","vscode":"vscode"}
def openappweb(query):
  if 'open vs code' in query: #open vs code
         speak("Opening vs code")
         codepath="C:\\Users\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codepath)
  elif 'open excel' in query: #open vs code
         speak("Opening  MS excel")
         codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
         os.startfile(codepath)
  elif 'open chrome' in query: #open vs code
         speak("Opening  chrome")
         codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
         os.startfile(codepath)

def closeappweb(query):
    speak("Closing sir")
    if 'one tab' in query or '1 tab' in query:
        pyautogui.hotkey('ctrl','w')
    elif '2 tab' in query or 'two tab' in query:
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        speak("All tab closed")
    elif '3 tab' in query or 'three tab' in query:
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        speak("All tab closed")
    elif '4 tab' in query or 'four tab' in query:
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        speak("All tab closed")
    elif '5 tab' in query or 'five tab' in query:
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        pyautogui.hotkey('ctrl','w')        
        sleep(0.5)
        speak("All tab closed")
    
    else:
        keys=list(dictapp.keys())
        for app in keys:
            if app in query :
                os.system(f"taskkill /f /in {dictapp[app]}.exe")