import os
from playsound import playsound
import datetime
import pyttsx3
import speech_recognition as sr


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

ext_time=open("D:\jarvis\Data.txt",'rt')
time=ext_time.read()
Time=str(time)

delete_time=open("D:\jarvis\Data.txt",'r+')
delete_time.truncate(0)
delete_time.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
     r=sr.Recognizer()

     with sr.Microphone() as source:
          print(":  Listening...")
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source,duration = 0.5)
          audio=r.listen(source,timeout=10,phrase_time_limit=3)
     try:
         print(":  Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(":  Your Command : "+query+"  \n")
     except:
         return ""
     
     return query.lower()

def ring(time):
    timetoset=str(time)
    timetoset=timetoset.replace("set alarm for ","")
    timetoset=timetoset.replace("alarm for","")
    timetoset=timetoset.replace(" and ",":")
    Alarm_time=str(timetoset)
    speak("Alarm set for "+Alarm_time)
    
    while True:
        current_time=datetime.datetime.now().strftime("%H:%M")
        if current_time==Alarm_time:
            print("Wake up sir, it's time. ")
            speak("Wake up sir, it's time")
            speak("Wake up sir, it's time")
            k=listen()
            if k=='stop the alarm':
                speak("Alarm stopped")
                break


 
