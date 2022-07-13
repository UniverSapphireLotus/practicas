# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 882)
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
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_3 = QHBoxLayout(self.page_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.scrollArea = QScrollArea(self.page_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1111, 647))
        self.horizontalLayout_7 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.horizontalLayout_7.addLayout(self.gridLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_3.addWidget(self.scrollArea)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_4 = QHBoxLayout(self.page_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.scrollArea_2 = QScrollArea(self.page_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1111, 647))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.horizontalLayout_6.addLayout(self.gridLayout_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_4.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.frame_3, 1, 0, 2, 3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))
        self.pushButton_2.setSizeIncrement(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(20, 20))
        self.pushButton_5.setMaximumSize(QSize(16777215, 40))
        self.pushButton_5.setSizeIncrement(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(20, 20))
        self.pushButton_4.setMaximumSize(QSize(16777215, 40))
        self.pushButton_4.setSizeIncrement(QSize(20, 20))

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 2)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(120, 120))
        self.toolButton.setSizeIncrement(QSize(120, 120))
        icon = QIcon()
        icon.addFile(u"pengu.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(120, 120))

        self.gridLayout.addWidget(self.toolButton, 0, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Intrusos", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Camaras", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"AGREGAR", None))
    # retranslateUi

