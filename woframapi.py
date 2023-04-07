import wolframalpha
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

apikey="8E5QH5-QUJYLUXT8T"

client=wolframalpha.Client(apikey)

def calculate(query):

    query = query.replace('calculate','')
    query = query.replace('into','*')
    query = query.replace('multiply','*')
    query = query.replace('plus','+')
    query = query.replace('minus','-')
    query = query.replace('divided by','/')

    res=client.query(query)
    try:
        info = next(res.results).text
        speak(str(info))
    except:
        speak("sir, I am unable to calculate that")

def temp(s):
    res=client.query(s)
    try:
        info = next(res.results).text
        speak(str(info))
    except:
        speak("sir, I am unable to fetch that")
        

    
