import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QMainWindow)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi


from wuv import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setupUi(self)

        #self.connectSignalsSlots()
        #self.label.mousePressEvent = self.mous_posi
        self.stackedWidget.setCurrentWidget(self.page_2)

        self.page_2 = daVincci(self.page_2)
        self.pos = None


    def connectSignalsSlots(self):

        #self.action_Exit.triggered.connect(self.close)
        pass

    def mous_posi(self, event):
        x= event.pos().x()
        y= event.pos().y()
        print(x," |-| " ,y)
        print(type(self.page))
        print(type(self))
        print(type(self.label))
        q = QPainter(self.label)
        #self.page= q
        #q.begin(self.page)
        q.drawLine(x, y, 250, 500)
        self.update()

    def paintEvent(self, event):
        if self.pos:
            q = QPainter(self)
            q.drawLine(self.pos.x(), self.pos.y(), 250, 500)

class daVincci(QWidget):
    def __init__(self, parent=None):
        super(daVincci, self).__init__(parent=parent)
        #self.mousePressEvent = self.paintEvent
        print(self.geometry())

    def paintEvent(self, event):
        print(event)
        print("raaaaa")
        
        x= event.pos().x()
        y= event.pos().y()
        print(x," |-| " ,y)
        #super().paintEvent()
        q = QPainter(self)
        q.begin(self) 
        q.drawLine(0, 0, 5000, 5000)

        #q.end() 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

#pyuic5 -x nikaido.ui -o wuv.py