# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speedtestui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SpeedTest(object):
    def setupUi(self, SpeedTest):
        SpeedTest.setObjectName("SpeedTest")
        SpeedTest.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SpeedTest)
        self.centralwidget.setObjectName("centralwidget")
        self.gif = QtWidgets.QLabel(self.centralwidget)
        self.gif.setGeometry(QtCore.QRect(0, 0, 801, 571))
        self.gif.setText("")
        self.gif.setPixmap(QtGui.QPixmap("D:\jarvis\database\gui stuffs\stgif.gif"))
        self.gif.setScaledContents(True)
        self.gif.setObjectName("gif")
        SpeedTest.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SpeedTest)
        self.statusbar.setObjectName("statusbar")
        SpeedTest.setStatusBar(self.statusbar)

        self.retranslateUi(SpeedTest)
        QtCore.QMetaObject.connectSlotsByName(SpeedTest)

    def retranslateUi(self, SpeedTest):
        _translate = QtCore.QCoreApplication.translate
        SpeedTest.setWindowTitle(_translate("SpeedTest", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SpeedTest = QtWidgets.QMainWindow()
    ui = Ui_SpeedTest()
    ui.setupUi(SpeedTest)
    SpeedTest.show()
    sys.exit(app.exec_())
