import pywhatkit,pyttsx3
import os
import webbrowser as web
import wikipedia
from pywikihow import WikiHow, search_wikihow
import requests
import webbrowser as wb
import speech_recognition as sr
from datetime import datetime

def GoogleSearch(term):
    query=term.replace("google search","")
    query=query.replace("what is","")
    query=query.replace("how to","")
    query=query.replace("what do you mean by","")
    query=query.replace("who is","")
    if len(query)==0:
        speak("please search again sir")
        return
    else:    
        writeab=str(query)

        kuchbhi=open("D:\\jarvis\\Data.txt",'a')
    #kuchbhi.write(writeab)
        kuchbhi.close()

        Query=str(term)
        pywhatkit.search(Query)

        if 'how to' in Query:
            max_result=1
            htf=search_wikihow(query=Query,max_results=max_result)
            assert len(htf)==1
            htf[0].print()
            speak(htf[0].summary)

        else:
            try:
                search=wikipedia.summary(Query,2)
                speak("As per your search "+search)
            except:
                speak("please try again with a different search key sir")        

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    print(audio+"\n")
    engine.say(audio)
    engine.runAndWait()

def ytsearch(term):
    result="https://www.youtube.com/results?search_query="+term
    web.open(result)
    speak("Good evening sir")
    speak("This is what i have found sir.")
    pywhatkit.playonyt(term)
    speak("This May also help you sir .")

def Alarm(query):
    timehere=open('D:\jarvis\Data.txt','a')
    timehere.write(query)
    timehere.close()
    #os.startfile("")

def ytdownload():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    from pyperclip import paste

    from time import sleep
    sleep(2)
    click(x=780,y=63)

    hotkey('ctrl','c')

    value=paste()

    Link=str(value)

    def download(link):
        url = YouTube(link)

        video=url.streams.first()

        video.download('D:\\jarvis\\database\\ytdownloads\\')

    download(Link)

    speak('sir, your video has been downloaded. ')
    speak('you can find the downloaded video here.')
    os.startfile('D:\\jarvis\\database\\ytdownloads\\')

def SpeedTest():
    os.startfile("D:\jarvis\database\gui_programs\speedtestgui.py")
    
def mylocation():
    ipadd =  requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
    loc  = 'https://www.google.com/maps/place/Sai+swathi+nivas+apartment+shop+employees+colony+road+3rd+line/@16.301314,80.4564877,15z/data=!3m1!4b1!4m6!3m5!1s0x3a4a0b342e064fc7:0xd293b8cafe77fd6b!8m2!3d16.3013142!4d80.465221!16s%2Fg%2F11j0yg2t24'
    #wb.open(loc)
    geo = requests.get(url)

    geo_d = geo.json()

    state = geo_d['city']

    country = geo_d['country']

    speak('sir , you are in {} {}'.format("guntur",country))

def listen():
     r=sr.Recognizer()

     with sr.Microphone() as source:
          print(":  Listening...")
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source,duration = 0.5)
          audio=r.listen(source,timeout=10,phrase_time_limit=5)
     try:
         print(":  Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(":  Your Command : "+query+"  \n")
     except:
         return ""
     
     return query.lower()

def notepad():
    speak("sir, i am ready to take a note")
    writes =  listen()

    time =datetime.now().strftime("%H:%M")
    #time =datetime.now().strftime("%H:%M")
    time=str(time)
    filename=time.replace(':','')
    filename=filename+'-note.txt'
    print(filename)
    with open(filename,"w") as file:
        file.write(writes)
    
    path1 = "D:\\jarvis\\" + str(filename)
    path2="D:\\jarvis\\database\\notepad\\"+str(filename)

    os.rename(path1,path2)
    os.startfile(path2)

    import time
    time.sleep(10)
    os.system("TASKKILL /F /im Notepad.exe")

def tellDay():
     

    day = datetime.today().weekday() + 1
     
    
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
     
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week+" sir")

def greet():
    speak("welcome sir, I am your personal assistant jarvis, how may i help you today")
          

