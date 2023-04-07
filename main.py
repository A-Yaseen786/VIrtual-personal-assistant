import pyttsx3
import speech_recognition as sr
from Features import *
import sys
from database.ExtraPro.start import GoogleImage
from database.ExtraPro.Alarm import ring
from automation import wtsmsg,wtscall
import time
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def speak_assist():
     engine.say("Welcome back sir")
     engine.runAndWait()

def listen():
     r=sr.Recognizer()

     with sr.Microphone() as source:
          print(":  Listening...")
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source, duration = 0.5)
          audio=r.listen(source,phrase_time_limit=5)
     try:
         print(":  Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(":  Your Command : "+query+"  \n")
     except Exception as e:
         return ""
     
     return query.lower()

def task():
     import facerec
     value = False
     while value == False:
          value = facerec.auth()
     greet()
     while True:
          query=listen()
          if 'youtube search' in query:
               query=query.replace("youtube search","")
               from Features import ytsearch
               ytsearch(query)

          elif 'google search' in query:
               query=query.replace("google search","")
               GoogleSearch(query)

          elif 'search image of' in query:
               from database.ExtraPro import start
               query=query.replace("search image of","")
               start.GoogleImage(query)

          elif 'exit' in query:
               speak("bye sir, have a good day")
               return
               
          elif 'send mail' in query:
               from database.ExtraPro import emauto
               emauto.send_mail()

          elif 'read inbox' in query:
               from database.ExtraPro import emauto

               emauto.read_mail()

          elif 'set alarm for ' in query:
               ring(query)

          elif 'download' in query:
               from Features import ytdownload
               ytdownload()

          elif 'internet speed' in query:
               from Features import SpeedTest
               SpeedTest()

          elif 'send message to' in query:
              name=query[15:]
              speak("please say the message sir")
              msg=listen()
              wtsmsg(name,msg)

          elif 'take a note' in query:
               from Features import notepad
               notepad()

          elif 'get my location' in query:
               from Features import mylocation
               mylocation()

          elif 'distance' in query:
               from dist import distance
               place = query.replace('distance to','')
               distance(str(place))

          elif 'jarvis what is the day today' in query:
               query = query.replace('jarvis','')
               tellDay()

          elif 'news' in query:
               from bbc import newsReader
               newsReader()

          elif 'go to sleep' in query:
               speak("sir, please enter How much time should i go to sleep")
               k=int(input())
               speak("going to sleep for "+str(k)+" minutes sir")
               time.sleep(k)
               speak("I am back sir")

          elif 'calculate' in query:
               from woframapi import calculate
               calculate(query)

          elif 'temperature' in query:
               from woframapi import temp
               query = query.replace('jarvis','')
               temp(query)

          elif 'make my sketch' in query:
               from sketch import capture
               capture()

          elif 'play game' in query:
              from mainGame import game
              score=0
              fin=game(score)
              speak(f"Your score : {fin}")
              print(f"Your score : {fin}")


          




             




   