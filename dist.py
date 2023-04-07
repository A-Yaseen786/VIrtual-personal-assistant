from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen
import math,pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def calculate(lat1, lon1, lat2, lon2):
    R = 6371 # This is the radius of earth in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = R * c
    return distance


def distance(place):
    print(place)
    locator = Nominatim(user_agent="myGeocoder")
    location = locator.geocode(place)
    if location == None:
        speak("Sir please recheck the target location")
        return 
    tlat = location.latitude
    tlong = location.longitude
    url ='http://ipinfo.io/json'
    response=urlopen(url)
    data=json.load(response)
    x=data['loc']
    x=x.split(',')
    clat=float(x[0])
    clong=float(x[1])
    k=calculate(clat,clong,tlat,tlong)
    speak("sir, the distance between your location and "+str(place)+" is "+str(int(k))+" kilometers")
    



