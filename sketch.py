import cv2 as cv
import os,pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def capture():
    cam = cv.VideoCapture(0)
    speak("Be steady sir i am making your sketch")
    result, image = cam.read()

    if result:
    
        cv.imshow("SketchMaker", image)
        cv.imwrite("D:\\jarvis\\database\\ExtraPro\\sketches\\sketch.png", image)
    
        
        cv.waitKey(0)  
    else:
        speak("No image detected sir. Please! try again")

    convert_sketch()    


def convert_sketch():
    image = cv.imread('D:\\jarvis\\database\\ExtraPro\\sketches\\sketch.png') 
    grey_img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    invert = cv.bitwise_not(grey_img)  
    blur = cv.GaussianBlur(invert, (21, 21), 0)
    invertedblur = cv.bitwise_not(blur)
    sketch = cv.divide(grey_img, 255-invertedblur, scale=256.0)
    cv.imwrite("D:\\jarvis\\database\\ExtraPro\\pencilsketches\\sketch1.png", sketch)
    speak("Here is your sketch sir")
    os.startfile("D:\\jarvis\\database\\ExtraPro\\pencilsketches\\sketch1.png")

