from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from database.gui_programs.jarvisUI import Ui_MainWindow
import sys
import main



class MainThread(QThread):

    def __init__(self): 

        super(MainThread,self).__init__()

    def run(self):
        self.Task_Gui()

    def Task_Gui(self):
        main.task()


startFunctions = MainThread() 


class Gui_Start(QMainWindow):

    def __init__(self):

        super().__init__()
           
        self.jarvis_ui = Ui_MainWindow()
        self.jarvis_ui.setupUi(self)
        

        self.jarvis_ui.pushButton.clicked.connect(self.close)


        self.jarvis_ui.pushButton_2.clicked.connect(self.startFunc)

    def startFunc(self):

        self.jarvis_ui.movies = QtGui.QMovie("D:\jarvis\database\gui stuffs\Hero_Template.gif")

        self.jarvis_ui.gif.setMovie(self.jarvis_ui.movies)

        self.jarvis_ui.movies.start()



        self.jarvis_ui.movies_2 = QtGui.QMovie("D:\jarvis\database\gui stuffs\Earth.gif")

        self.jarvis_ui.gif2.setMovie(self.jarvis_ui.movies_2)

        self.jarvis_ui.movies_2.start()




        self.jarvis_ui.movies_3 = QtGui.QMovie("D:\jarvis\database\gui stuffs\__02-____.gif")

        self.jarvis_ui.gif3.setMovie(self.jarvis_ui.movies_3)

        self.jarvis_ui.movies_3.start()


        self.jarvis_ui.movies_4 = QtGui.QMovie("D:\jarvis\database\gui stuffs\code_template.gif")

        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies_4)

        self.jarvis_ui.movies_4.start()



        timer = QTimer(self)

        timer.timeout.connect(self.showtime)

        timer.start(1000)

        startFunctions.start()

    def showtime(self):
        
        current_time = QTime.currentTime()

        label_time = current_time.toString("hh:mm:ss")

        labbel = " Time :  " + label_time 

        self.jarvis_ui.textBrowser.setText(labbel)




Gui_App = QApplication(sys.argv)

Gui_Jarvis = Gui_Start()

Gui_Jarvis.show()
exit(Gui_App.exec_())
















