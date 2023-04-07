import os
import selenium
import webbrowser as web
from GoogleImageScrapper.GoogleImageScrapper import GoogleImageScraper
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
def GoogleImage(term):
    query=str(term)
    if len(query)==0:
        speak("please come again sir")
    else:    
        url="https://www.google.co.in/images?q="+query
        web.open(url)
    
