# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 603)
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
        self.frame.setGeometry(QRect(0, 130, 441, 441))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 4, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(120, 120))
        self.toolButton.setSizeIncrement(QSize(120, 120))
        icon = QIcon()
        icon.addFile(u"pengu.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(120, 120))

        self.gridLayout.addWidget(self.toolButton, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(20, 20))
        self.pushButton.setMaximumSize(QSize(16777215, 40))
        self.pushButton.setSizeIncrement(QSize(20, 20))

        self.gridLayout.addWidget(self.pushButton, 9, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(20, 20))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))
        self.pushButton_2.setSizeIncrement(QSize(20, 20))

        self.gridLayout.addWidget(self.pushButton_2, 10, 0, 1, 2)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 6, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"Contrasena", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"Usuario nuevo", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Iniciar scanner", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"cancelar", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"Repetir contrasena", None))
    # retranslateUi

