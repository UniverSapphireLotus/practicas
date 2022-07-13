# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(470, 574)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setSizeIncrement(QSize(0, 0))
        MainWindow.setStyleSheet(u"*{\n"
"	font-family: century gothyc;\n"
"	font-size: 24px;\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	background-color: rgb(51, 51, 51);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QToolButton{\n"
"	background: rgb(156, 0, 1);\n"
"	border-radius: 60px;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color:  rgb(51, 51, 51);\n"
"	background: rgb(156, 0, 1);\n"
"	border-radius: 20px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(156, 0, 1);\n"
"	border-radius: 20px;\n"
"	background: rgb(51, 51, 51);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background:transparent;	\n"
"	border-color: rgb(84, 150, 255);\n"
"	border: none;\n"
"	color:rgb(113, 112, 114);\n"
"\n"
"	border-bottom: 1px solid rgb(113, 112, 114);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 130, 461, 381))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(170, 40, 111, 31))
        self.label.setStyleSheet(u"")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 320, 381, 40))
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setSizeIncrement(QSize(20, 20))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(60, 120, 341, 71))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(60, 220, 341, 71))
        self.toolButton = QToolButton(self.centralwidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(160, 40, 120, 120))
        self.toolButton.setMinimumSize(QSize(120, 120))
        self.toolButton.setSizeIncrement(QSize(120, 120))
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(120, 120))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"INGRESAR", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

