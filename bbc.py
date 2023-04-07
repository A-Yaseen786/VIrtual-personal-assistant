import requests as req
from bs4 import BeautifulSoup
import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

request = req.get('https://www.bbc.com/news')
html = request.content
soup = BeautifulSoup(html,'html.parser')

def newsReader():
    nl = []
    for h in soup.find_all('h3',class_='gs-c-promo-heading__title'):
        news_title = h.contents[0].lower()
        if news_title not in nl:
            if 'bbc' not in news_title:
                nl.append(news_title)

    speak("sir, here are some news that i fetched as per your request")
    for i in nl[:6]:
        speak(str(i))

