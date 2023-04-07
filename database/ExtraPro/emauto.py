import os
from email.message import EmailMessage
import ssl
import smtplib
import email,pyttsx3
import speech_recognition as sr


def listen():
     r=sr.Recognizer()

     with sr.Microphone() as source:
          print(":  Listening...")
          r.pause_threshold=1
          r.adjust_for_ambient_noise(source, duration = 0.5)
          audio=r.listen(source,phrase_time_limit=8)
     try:
         print(":  Recognizing...")
         query=r.recognize_google(audio,language='en-in')
         print(":  Your Command : "+query+"  \n")
     except Exception as e:
         return ""
     
     return query.lower()

sender = "yabd7866@gmail.com"
empass = "xebntndyrvjhrjzj"
em = EmailMessage()

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)


def speak(audio):
    print(audio+"\n")
    engine.say(audio)
    engine.runAndWait()

def send_mail():
    speak("Whom do you want to send the mail sir.")
    mail=listen()
    newm=""
    for i in range(len(mail)):
        if mail[i] != " ":
            newm+=mail[i]
    newm=newm+"@gmail.com"
    receiver = newm
    sub = "testing email automation "
    speak("what is the message sir.")
    mess = listen()
    body = str(mess)
    
    em['From'] = sender
    em["To"] = receiver
    em['Subject'] = sub
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(sender,empass)
        smtp.sendmail(sender,receiver,em.as_string())

    speak("Email sent sir.")

def read_mail():
    imap_server = "imap.gmail.com"
    import imaplib
    imap = imaplib.IMAP4_SSL(imap_server)
    imap.login(sender,empass)
    imap.select("inbox")
    response, messages=imap.search(None, 'UnSeen')
    speak("I am checking for new mails sir.")
    if len(messages) <=1 and messages[0] == b'':
        print("No new mails")
        speak("No new mails sir")
    else:    
        messages = messages[0].split()
        msgcount = len(messages)
        latest = int(messages[-1])
        oldest = int(messages[0])
        for i in range(latest, latest-msgcount, -1):
            # fetching mails from inbox using imap
            res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    print()
                    print(msg["Date"])
                    print(msg["From"])
                    print(msg["Subject"])
                    speak("Mail from "+str(msg["From"]))
                    speak(str(msg["Subject"]))
                    
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode = True)
                print("entered body loop")
                print(f'Body: {body.decode("UTF-8")}', )
                speak(str(f'Body: {body.decode("UTF-8")}'))
             
    

  


