from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore ,QtWidgets,QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import pyttsx3
from speedtestui import Ui_SpeedTest
import sys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',170)

def speak(audio):
    print(audio+"\n")
    engine.say(audio)
    engine.runAndWait()

def run_uit():

    speak("I am checking the internet speed sir")

    import speedtest
    speed =speedtest.Speedtest()
    upload = speed.upload()

    correct=int(int(upload)/80000)

    download=speed.download()

    correct_down=int(int(download)/80000)

    speak("Downloading speed is "+str(correct_down)+" Mbps")
    speak("Uploading speed is "+str(correct)+" Mbps")

    sys.exit()



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        run_uit()

StartExe = MainThread()

class StartExecution(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_SpeedTest()
        self.ui.setupUi(self)
        self.ui.label=QMovie("D:\jarvis\database\gui stuffs\stgif.gif")
        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        StartExe.start()

App=QApplication(sys.argv)
speedtest=StartExecution()
speedtest.show()
sys.exit(App.exec_())