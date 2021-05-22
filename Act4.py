#Authors:
#Franco Minutti Simoni - A01733927
#Alan Mondragón Rivas - A01734565
#Created 20 May, 2021
# This program functions as an mp3 player in a digital interface.

import os
from PyQt5 import QtGui, QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
import math
import numpy as np
import pygame
import eyed3
import time

song_num = 0
state = True

class Ui_MainWindow(object):
    song_num = 0
    state = True
#Reproduces the selected song, with te given conditions
    def Reproduce(self,play):
        global song_num
        pygame.mixer.init()
        if (song_num == 0):
            pygame.mixer.music.load("alan-walker-sing-me-to-sleep.mp3")
            audiofile = eyed3.load("alan-walker-sing-me-to-sleep.mp3")
        elif(song_num == 1):
            pygame.mixer.music.load("avicii-waiting-for-love.mp3")
            audiofile = eyed3.load("avicii-waiting-for-love.mp3")
        elif(song_num == 2):
            pygame.mixer.music.load("axwell-l-ingrosso-more-than-you-know-official-video.mp3")
            audiofile = eyed3.load("axwell-l-ingrosso-more-than-you-know-official-video.mp3")
        elif(song_num == 3):
            pygame.mixer.music.load("dua-lipa-levitating-featuring-dababy-official-music-video.mp3")
            audiofile = eyed3.load("dua-lipa-levitating-featuring-dababy-official-music-video.mp3")
        elif(song_num == 4):
            pygame.mixer.music.load("far-east-movement-ryan-tedder-rocketeer-ft-ryan-tedder.mp3")
            audiofile = eyed3.load("far-east-movement-ryan-tedder-rocketeer-ft-ryan-tedder.mp3")
        elif(song_num == 5):
            pygame.mixer.music.load("j-balvin-khalid-otra-noche-sin-ti-official-video.mp3")
            audiofile = eyed3.load("j-balvin-khalid-otra-noche-sin-ti-official-video.mp3")
        elif(song_num == 6):
            pygame.mixer.music.load("sam-smith-how-do-you-sleep-official-video.mp3")
            audiofile = eyed3.load("sam-smith-how-do-you-sleep-official-video.mp3")
        elif(song_num == 7):
            pygame.mixer.music.load("stephen-crossfire.mp3")
            audiofile = eyed3.load("stephen-crossfire.mp3")
        elif(song_num == 8):
            pygame.mixer.music.load("the-script-hall-of-fame-ft-william-traducida-al-espanol.mp3")
            audiofile = eyed3.load("the-script-hall-of-fame-ft-william-traducida-al-espanol.mp3")
        elif(song_num == 9):
            pygame.mixer.music.load("timmy-trumpet-savage-freaks-official-video.mp3")
            audiofile = eyed3.load("timmy-trumpet-savage-freaks-official-video.mp3")
        else:
            print("Error: ", song_num)
        if (play == 1):
            pygame.mixer.music.play()
            self.label.setText(str(audiofile.tag.title)+"\n"+str(audiofile.tag.artist)+"\n"+str(audiofile.tag.album)+"\n"+str(audiofile.tag.track_num)+"\n"+str(pygame.mixer.music.get_pos()))
        else:
            pygame.mixer.music.pause()
#Goes to the next song
    def Next(self):
        global song_num
        if (song_num>8):
            song_num = 0
        else:
            song_num += 1
        self.Reproduce(1)
#Intercalates between Pause and Play the songs
    def PlayPause(self):
        global state
        if (state == True):
            state = False
            pygame.mixer.music.pause()

        else:
            state = True
            pygame.mixer.music.unpause()
#Goes to the Previous song
    def Previous(self):
        global song_num
        if (song_num<1):
            song_num = 9
        else:
            song_num -= 1
        self.Reproduce(1)
#Restarts the playlist
    def Stop(self):
        global song_num
        song_num = 0
        self.Reproduce(1)
#Detects what button was pressed
    def Press(self,x):
        global song_num
        if (x == 0):
            song_num = 0
        elif(x == 1):
            song_num = 1
        elif(x == 2):
            song_num = 2
        elif(x == 3):
            song_num = 3
        elif(x == 4):
            song_num = 4
        elif(x == 5):
            song_num = 5
        elif(x == 6):
            song_num = 6
        elif(x == 7):
            song_num = 7
        elif(x == 8):
            song_num = 8
        elif(x == 9):
            song_num = 9
        self.Reproduce(1)

#Setup the ui
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(955, 872)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push0 = QtWidgets.QPushButton(self.centralwidget)
        self.push0.setGeometry(QtCore.QRect(30, 30, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push0.setFont(font)
        self.push0.setObjectName("push0")
        self.push1 = QtWidgets.QPushButton(self.centralwidget)
        self.push1.setGeometry(QtCore.QRect(30, 90, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push1.setFont(font)
        self.push1.setObjectName("push1")
        self.push2 = QtWidgets.QPushButton(self.centralwidget)
        self.push2.setGeometry(QtCore.QRect(30, 150, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push2.setFont(font)
        self.push2.setObjectName("push2")
        self.push4 = QtWidgets.QPushButton(self.centralwidget)
        self.push4.setGeometry(QtCore.QRect(30, 270, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push4.setFont(font)
        self.push4.setObjectName("push4")
        self.push3 = QtWidgets.QPushButton(self.centralwidget)
        self.push3.setGeometry(QtCore.QRect(30, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push3.setFont(font)
        self.push3.setObjectName("push3")
        self.push5 = QtWidgets.QPushButton(self.centralwidget)
        self.push5.setGeometry(QtCore.QRect(30, 330, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push5.setFont(font)
        self.push5.setObjectName("push5")
        self.push7 = QtWidgets.QPushButton(self.centralwidget)
        self.push7.setGeometry(QtCore.QRect(30, 450, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push7.setFont(font)
        self.push7.setObjectName("push7")
        self.push6 = QtWidgets.QPushButton(self.centralwidget)
        self.push6.setGeometry(QtCore.QRect(30, 390, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push6.setFont(font)
        self.push6.setObjectName("push6")
        self.push8 = QtWidgets.QPushButton(self.centralwidget)
        self.push8.setGeometry(QtCore.QRect(30, 510, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push8.setFont(font)
        self.push8.setObjectName("push8")
        self.push9 = QtWidgets.QPushButton(self.centralwidget)
        self.push9.setGeometry(QtCore.QRect(30, 570, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.push9.setFont(font)
        self.push9.setObjectName("push9")
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(120, 40, 411, 41))
        self.label_0.setObjectName("label_0")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(120, 100, 411, 41))
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 160, 411, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 220, 411, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 280, 411, 41))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(120, 400, 411, 41))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 340, 411, 41))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(120, 450, 411, 41))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 570, 411, 41))
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 510, 411, 41))
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(600, 90, 291, 471))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.prev_2 = QtWidgets.QPushButton(self.centralwidget)
        self.prev_2.setGeometry(QtCore.QRect(300, 620, 91, 91))
        self.prev_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("prev.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prev_2.setIcon(icon)
        self.prev_2.setIconSize(QtCore.QSize(150, 150))
        self.prev_2.setCheckable(False)
        self.prev_2.setAutoRepeat(False)
        self.prev_2.setAutoExclusive(False)
        self.prev_2.setAutoDefault(True)
        self.prev_2.setDefault(True)
        self.prev_2.setObjectName("prev_2")
        self.play_pause = QtWidgets.QPushButton(self.centralwidget)
        self.play_pause.setGeometry(QtCore.QRect(410, 620, 91, 91))
        self.play_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("play_pause.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_pause.setIcon(icon1)
        self.play_pause.setIconSize(QtCore.QSize(150, 150))
        self.play_pause.setAutoDefault(True)
        self.play_pause.setDefault(True)
        self.play_pause.setObjectName("play_pause")
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(630, 620, 91, 91))
        self.next.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("next.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next.setIcon(icon2)
        self.next.setIconSize(QtCore.QSize(150, 150))
        self.next.setDefault(True)
        self.next.setObjectName("next")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(520, 620, 91, 91))
        self.stop.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("stop.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stop.setIcon(icon3)
        self.stop.setIconSize(QtCore.QSize(150, 150))
        self.stop.setAutoDefault(True)
        self.stop.setDefault(True)
        self.stop.setObjectName("stop")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 955, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.push0.clicked.connect(lambda:self.Press(0))
        self.push1.clicked.connect(lambda:self.Press(1))
        self.push2.clicked.connect(lambda:self.Press(2))
        self.push3.clicked.connect(lambda:self.Press(3))
        self.push4.clicked.connect(lambda:self.Press(4))
        self.push5.clicked.connect(lambda:self.Press(5))
        self.push6.clicked.connect(lambda:self.Press(6))
        self.push7.clicked.connect(lambda:self.Press(7))
        self.push8.clicked.connect(lambda:self.Press(8))
        self.push9.clicked.connect(lambda:self.Press(9))
        self.prev_2.clicked.connect(self.Previous)
        self.play_pause.clicked.connect(self.PlayPause)
        self.next.clicked.connect(self.Next)
        self.stop.clicked.connect(self.Stop)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.push0.setText(_translate("MainWindow", "0"))
        self.push1.setText(_translate("MainWindow", "1"))
        self.push2.setText(_translate("MainWindow", "2"))
        self.push4.setText(_translate("MainWindow", "4"))
        self.push3.setText(_translate("MainWindow", "3"))
        self.push5.setText(_translate("MainWindow", "5"))
        self.push7.setText(_translate("MainWindow", "7"))
        self.push6.setText(_translate("MainWindow", "6"))
        self.push8.setText(_translate("MainWindow", "8"))
        self.push9.setText(_translate("MainWindow", "9"))
        self.label_0.setText(_translate("MainWindow", "alan-walker-sing-me-to-sleep"))
        self.label_1.setText(_translate("MainWindow", "avicii-waiting-for-love"))
        self.label_2.setText(_translate("MainWindow", "axwell-l-ingrosso-more-than-you-know-official-video"))
        self.label_3.setText(_translate("MainWindow", "dua-lipa-levitating-featuring-dababy-official-music-video"))
        self.label_4.setText(_translate("MainWindow", "far-east-movement-ryan-tedder-rocketeer-ft-ryan-tedder"))
        self.label_5.setText(_translate("MainWindow", "j-balvin-khalid-otra-noche-sin-ti-official-video"))
        self.label_6.setText(_translate("MainWindow", "sam-smith-how-do-you-sleep-official-video"))
        self.label_7.setText(_translate("MainWindow", "stephen-crossfire"))
        self.label_8.setText(_translate("MainWindow", "the-script-hall-of-fame-ft-william-traducida-al-espanol"))
        self.label_9.setText(_translate("MainWindow", "timmy-trumpet-savage-freaks-official-video"))
        self.label.setText(_translate("MainWindow","---"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
