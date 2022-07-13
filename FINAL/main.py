import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import *


from login import Ui_MainWindow as login_Ui_MainWindow
from register import Ui_MainWindow as regis_Ui_MainWindow
from panel import Ui_MainWindow as panel_Ui_MainWindow

from IGOR import capturar_, reconocer_, generar_

import os

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #self.panel= RegisterWindow()
        self.panel= PanelWindow()

        self.ui =login_Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(lambda: self.log_user())
        self.ui.pushButton_2.clicked.connect(lambda: self.close())
        self.show()

    def log_user(self):
        print("Wxw[<o_o>]mxM")
        user_name= self.ui.lineEdit.text()
        user_pass= self.ui.lineEdit_2.text()
        user_code= self.ui.lineEdit.text()

        ini= reconocer_.reconocer(0)
        print(user_name, " [__<-_->__] ",user_pass," [__<-_->__] ",user_code)
        print("Ww|7_7|wW", ini, "Ww|7_7|wW")

        if ini == True:
            self.close()
            self.panel.show()

            self.ui.lineEdit.setText("ACCESO CONCEDIDO")

        

class RegisterWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #self.login= RegisterWindow()
        

        self.ui =regis_Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(lambda: self.reg_user())
        self.ui.pushButton_2.clicked.connect(lambda: self.close())

        self.ui.toolButton.clicked.connect(lambda: self.analizar())
        #self.show()

    def reg_user(self):
        print("Wxw[<o_o>]mxM")
        user_name= self.ui.lineEdit.text()
        user_pass= self.ui.lineEdit_2.text()
        user_code= self.ui.lineEdit_3.text()

        print(user_name, " [__<-_->__] ",user_pass," [__<-_->__] ",user_code)

        capturar_.capturar(user_name)

    def analizar(self):
        generar_.generar()

class PanelWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #self.login= RegisterWindow()
        self.regis= RegisterWindow()

        self.ui =panel_Ui_MainWindow()
        self.ui.setupUi(self)

        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        #self.ui.pushButton.clicked.connect(lambda: self.reg_user())
        self.ui.toolButton.clicked.connect(lambda: self.reg_user())
        self.ui.pushButton_2.clicked.connect(lambda: self.panel_permitidos())
        self.ui.pushButton_5.clicked.connect(lambda: self.panel_intrusos())
        self.ui.pushButton_4.clicked.connect(lambda: self.detectar())
        #self.show()

        ####<><><><><>
        self.visa_allowed= os.path.dirname(__file__ ) + '\\IGOR\\capturas\\'+ 'permitido'
        self.visa_denied= os.path.dirname(__file__ ) + '\\IGOR\\capturas\\'+ 'intrusos'

        if not os.path.exists(self.visa_allowed):
            os.makedirs(self.visa_allowed)

        if not os.path.exists(self.visa_denied):
            os.makedirs(self.visa_denied)

        #print(os.listdir(visa_allowed))
        #print(os.listdir(visa_denied))
        print("~~~*'-_-'*~~~")
        """for i in os.listdir(visa_allowed):
            print(i)
        for i in os.listdir(visa_denied):
            print(i)"""

        for file in os.listdir(self.visa_allowed):
            pixmap = QPixmap(os.path.join(self.visa_allowed, file))
            cita= QLabel()
            cita.setText(file)
            if not pixmap.isNull():
                label = QLabel(pixmap=pixmap)
                #lay.addWidget(label)
                self.ui.gridLayout_2.addWidget(label)
                self.ui.gridLayout_2.addWidget(cita)
                

        for file in os.listdir(self.visa_denied):
            pixmap = QPixmap(os.path.join(self.visa_denied, file))
            cita= QLabel()
            cita.setText(file)
            if not pixmap.isNull():
                label = QLabel(pixmap=pixmap)
                #lay.addWidget(label)
                self.ui.gridLayout_3.addWidget(label)
                self.ui.gridLayout_3.addWidget(cita)



    def reg_user(self):
        print("Wxw[<o_o>]mxM")
        self.regis.show()

    def detectar(self):
        print("Wxw[<o_o>]mxM")
        reconocer_.detectar()

    def panel_permitidos(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        for i in reversed(range(self.ui.gridLayout_2.count())): 
            self.ui.gridLayout_2.itemAt(i).widget().setParent(None)

        for file in os.listdir(self.visa_allowed):
            pixmap = QPixmap(os.path.join(self.visa_allowed, file))
            cita= QLabel()
            cita.setText(file)
            if not pixmap.isNull():
                label = QLabel(pixmap=pixmap)
                #lay.addWidget(label)
                self.ui.gridLayout_2.addWidget(label)
                self.ui.gridLayout_2.addWidget(cita)



    def panel_intrusos(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)
        for i in reversed(range(self.ui.gridLayout_3.count())): 
            self.ui.gridLayout_3.itemAt(i).widget().setParent(None)

        for file in os.listdir(self.visa_denied):
            pixmap = QPixmap(os.path.join(self.visa_denied, file))
            cita= QLabel()
            cita.setText(file)
            if not pixmap.isNull():
                label = QLabel(pixmap=pixmap)
                #lay.addWidget(label)
                self.ui.gridLayout_3.addWidget(label)
                self.ui.gridLayout_3.addWidget(cita)
        

        



if __name__== '__main__':
    print('raaaa')
    app= QApplication(sys.argv)
    window= MainWindow()
    #panel= RegisterWindow()
    sys.exit(app.exec_())

#pyside6-uic mainwindow.ui > ui_mainwindow.py
#pyside6-uic login.ui -o login.py
#pyside6-uic panel.ui -o panel.py

