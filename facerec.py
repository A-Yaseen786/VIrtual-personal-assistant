from deepface import DeepFace as df
import cv2 as cv
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def auth():
    speak("Face recognition in progress please look into the webcam")

    cam = cv.VideoCapture(0)
    result, image = cam.read()
    cv.imwrite("D:\\jarvis\\database\\pics\\sketch.jpg", image)
    try:
        result = df.verify("D:\\jarvis\\database\\gui stuffs\\authentication_image.jpg","D:\\jarvis\\database\\pics\\sketch.jpg")
        if result["verified"] == True:
            return True

    except:
        speak("No face detected")
        return False    
