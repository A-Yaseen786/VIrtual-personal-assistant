from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
import pywhatkit as p
import datetime,pyttsx3
from time import sleep
from geopy.distance import great_circle
import geocoder
from geopy.geocoders import Nominatim

import webbrowser as wb
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    print(audio+"\n")
    engine.say(audio)
    engine.runAndWait()

def wtsmsg(name,message):

    startfile("C:\\Users\\yasee\\OneDrive\\Desktop\\WhatsApp Web.lnk")
    sleep(15)
    click(x=265,y=165)
    sleep(1)
    write(name)
    sleep(1)
    click(x=383,y=319)
    sleep(1)
    click(x=1181,y=962)
    sleep(1)
    write(message)
    sleep(1)
    click(x=1853,y=952)
    speak("Message sent sir")

def wtscall(name):
    speak("calling "+str(name))
    startfile("C:\\Users\\yasee\\OneDrive\\Desktop\\WhatsApp Web.lnk")
    sleep(10)
    click(x=265,y=165)
    sleep(1)
    write(name)
    sleep(1)
    click(x=383,y=319)
    sleep(2)
    click(x=1777,y=75)

def googlemaps(place):
    urlplace='http://www.google.com/maps/place/'+str(place)
    
    geolocator = Nominatim(user_agent="myGeocoder")
    location = geolocator.geocode(place,addressdetails=True)

    target_latlon = location.latitude, location.longitude

    location = location.raw['address']
    target = {'city':str(location.get('city','')),
             'state':str(location.get('state','')),
             'country':str(location.get('country',''))}
    
    current_loca=geocoder.ip('me')
    current_latlon= current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))

    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    #speak(target)
    speak('sir ,{} is {} kilometers away from your location'.format(place,distance))
    wb.open(urlplace)

#googlemaps('paris')  