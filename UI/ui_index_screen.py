# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index_screen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import files_rc
import files_rc

class Ui_IndexScreen(object):
    def setupUi(self, IndexScreen):
        if not IndexScreen.objectName():
            IndexScreen.setObjectName(u"IndexScreen")
        IndexScreen.resize(800, 600)
        self.centralwidget = QWidget(IndexScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setAutoFillBackground(False)
        self.mainFrame.setStyleSheet(u"")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.backgroundLabel = QLabel(self.mainFrame)
        self.backgroundLabel.setObjectName(u"backgroundLabel")
        self.backgroundLabel.setGeometry(QRect(0, 0, 800, 600))
        self.backgroundLabel.setPixmap(QPixmap(u":/image/images/backgrounds/index.png"))
        self.backgroundLabel.setScaledContents(True)
        self.startButton = QPushButton(self.mainFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(67, 387, 312, 69))
        self.startButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.startButton.setStyleSheet(u"\n"
"	background-color: transparent;\n"
"	border: 0;\n"
"")
        icon = QIcon()
        icon.addFile(u":/image/images/sentences/startButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.startButton.setIcon(icon)
        self.startButton.setIconSize(QSize(306, 63))
        self.finishButton = QPushButton(self.mainFrame)
        self.finishButton.setObjectName(u"finishButton")
        self.finishButton.setGeometry(QRect(147, 497, 312, 69))
        self.finishButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.finishButton.setStyleSheet(u"QPushButton {\n"
"	background-color: transparent;\n"
"	border: 0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/image/images/sentences/finishButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.finishButton.setIcon(icon1)
        self.finishButton.setIconSize(QSize(306, 63))
        self.osanaButton1 = QPushButton(self.mainFrame)
        self.osanaButton1.setObjectName(u"osanaButton1")
        self.osanaButton1.setGeometry(QRect(570, 70, 191, 351))
        self.osanaButton1.setCursor(QCursor(Qt.PointingHandCursor))
        self.osanaButton1.setStyleSheet(u"QPushButton{background: transparent;}")
        self.osanaButton2 = QPushButton(self.mainFrame)
        self.osanaButton2.setObjectName(u"osanaButton2")
        self.osanaButton2.setGeometry(QRect(500, 390, 191, 211))
        self.osanaButton2.setCursor(QCursor(Qt.PointingHandCursor))
        self.osanaButton2.setStyleSheet(u"QPushButton{background: transparent;}")
        self.moodDisplayLabel = QLabel(self.mainFrame)
        self.moodDisplayLabel.setObjectName(u"moodDisplayLabel")
        self.moodDisplayLabel.setGeometry(QRect(30, 280, 400, 60))
        self.moodDisplayLabel.setPixmap(QPixmap(u":/image/images/sentences/mood_normal.png"))
        self.moodDisplayLabel.setScaledContents(True)
        self.moodUpButton = QPushButton(self.mainFrame)
        self.moodUpButton.setObjectName(u"moodUpButton")
        self.moodUpButton.setGeometry(QRect(440, 275, 35, 35))
        font = QFont()
        font.setFamily(u"MS UI Gothic")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.moodUpButton.setFont(font)
        self.moodUpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.moodUpButton.setStyleSheet(u"font: 28pt \"MS UI Gothic\";\n"
"color: red;\n"
"background-color: transparent;")
        icon2 = QIcon()
        icon2.addFile(u":/image/images/icons/smallUpButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moodUpButton.setIcon(icon2)
        self.moodUpButton.setIconSize(QSize(30, 27))
        self.moodDownButton = QPushButton(self.mainFrame)
        self.moodDownButton.setObjectName(u"moodDownButton")
        self.moodDownButton.setGeometry(QRect(440, 305, 35, 35))
        self.moodDownButton.setFont(font)
        self.moodDownButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.moodDownButton.setStyleSheet(u"font: 28pt \"MS UI Gothic\";\n"
"color: blue;\n"
"background-color: transparent;")
        icon3 = QIcon()
        icon3.addFile(u":/image/images/icons/smallDownButton.png", QSize(), QIcon.Normal, QIcon.Off)
        self.moodDownButton.setIcon(icon3)
        self.moodDownButton.setIconSize(QSize(30, 27))
        self.moodUpLabel = QLabel(self.mainFrame)
        self.moodUpLabel.setObjectName(u"moodUpLabel")
        self.moodUpLabel.setGeometry(QRect(460, 240, 70, 50))
        self.moodUpLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: rgba(255, 169, 0, 1);")
        self.moodDownLabel = QLabel(self.mainFrame)
        self.moodDownLabel.setObjectName(u"moodDownLabel")
        self.moodDownLabel.setGeometry(QRect(460, 330, 70, 50))
        self.moodDownLabel.setStyleSheet(u"font: 75 26pt \"UD \u30c7\u30b8\u30bf\u30eb \u6559\u79d1\u66f8\u4f53 N-B\";\n"
"color: rgba(18, 93, 152, 1);")
        self.moodParameterBar = QProgressBar(self.mainFrame)
        self.moodParameterBar.setObjectName(u"moodParameterBar")
        self.moodParameterBar.setGeometry(QRect(30, 327, 401, 13))
        self.moodParameterBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 #f64f59, stop:0.5 #c471ed ,stop:1 #12c2e9);\n"
"	color: rgb(200, 200, 200);\n"
"	border-style: none;\n"
"}\n"
"QProgressBar::chunk{\n"
"	background-color: rgb(98, 114, 164);\n"
"}")
        self.moodParameterBar.setValue(32)
        self.moodParameterBar.setTextVisible(False)
        self.moodParameterBar.setInvertedAppearance(True)
        self.moodLabel = QLabel(self.mainFrame)
        self.moodLabel.setObjectName(u"moodLabel")
        self.moodLabel.setGeometry(QRect(10, 257, 482, 100))
        self.moodLabel.setStyleSheet(u"QLabel#moodLabel {\n"
"	background-color: rgba(0, 0, 0, .2);\n"
"	border-radius: 15px;\n"
"}")
        self.logoLabel = QLabel(self.mainFrame)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setGeometry(QRect(40, 30, 475, 170))
        self.logoLabel.setPixmap(QPixmap(u":/image/images/logos/title_logo.png"))
        self.logoLabel.setScaledContents(True)
        self.backgroundLabel.raise_()
        self.moodLabel.raise_()
        self.startButton.raise_()
        self.finishButton.raise_()
        self.osanaButton1.raise_()
        self.osanaButton2.raise_()
        self.moodDisplayLabel.raise_()
        self.moodUpButton.raise_()
        self.moodDownButton.raise_()
        self.moodUpLabel.raise_()
        self.moodDownLabel.raise_()
        self.moodParameterBar.raise_()
        self.logoLabel.raise_()

        self.verticalLayout.addWidget(self.mainFrame)

        IndexScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(IndexScreen)

        QMetaObject.connectSlotsByName(IndexScreen)
    # setupUi

    def retranslateUi(self, IndexScreen):
        IndexScreen.setWindowTitle(QCoreApplication.translate("IndexScreen", u"IndexScreen", None))
        self.backgroundLabel.setText("")
        self.startButton.setText("")
        self.finishButton.setText("")
        self.osanaButton1.setText("")
        self.osanaButton2.setText("")
        self.moodDisplayLabel.setText("")
        self.moodUpButton.setText("")
        self.moodDownButton.setText("")
        self.moodUpLabel.setText(QCoreApplication.translate("IndexScreen", u"+10", None))
        self.moodDownLabel.setText(QCoreApplication.translate("IndexScreen", u"-10", None))
        self.moodParameterBar.setFormat(QCoreApplication.translate("IndexScreen", u"%p", None))
        self.moodLabel.setText("")
        self.logoLabel.setText("")
    # retranslateUi

