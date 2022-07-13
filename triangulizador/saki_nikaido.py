import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from pyqtgraph.graphicsItems.PlotDataItem import dataType

# from PySide2 import QtWidgets
# from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

#import seabornplot

from nikaido import Ui_MainWindow



class MainWindow(QMainWindow):
    siz1= 0
    siz2= 0

    sizx= 0
    sizy= 0

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        #self.setWindowFlag(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.boto_menu.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_menu, self.siz1, self.sizx))
        self.ui.boto_tool.clicked.connect(lambda: self.move_menu(self.ui.frame_barra_tool, self.siz2, self.sizy))
        self.ui.boto_tool.setMaximumSize(0,0)

        
        self.ui.boto_max.hide()
        
        ####BOTO####
        self.ui.boto_cerrar.clicked.connect(lambda: self.close())
        self.ui.boto_max.clicked.connect(lambda: self.maxi_window())
        self.ui.boto_restaurar.clicked.connect(self.rest_window)
        self.ui.boto_min.clicked.connect(self.showMinimized)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.page.mousePressEvent = self.obtener_coordenada

        self.showMaximized()
        self.show()
  

    def move_menu(self, menu, lonx, lony):
        #self.clickPosition = event.globalPos()
        vi= menu.width()
        print('vi: ', vi)
        #cait= self.ui.frame_barra_menu.size()

        extend=0
        
        #self.ui.frame_barra_menu
        
        if vi==0:
            extend= lonx
            menu.setMinimumSize(extend,lony)
            #menu.setMaximumWidth(extend)
            #self.ui.frame_barra_menu.setMaximumWidth
        else:
            #self.siz1= menu.size().width()
            self.update_data()
            menu.setMaximumSize(extend,lony)
            print('oh me ejecuto')
            #self.ui.frame_barra_menu.resize(extend,844)
            #self.ui.frame_barra_menu.setGeometry()

        self.animacion = QPropertyAnimation(menu, b'minimumWidth')
        self.animacion.setDuration(400)
        self.animacion.setStartValue(vi)
        self.animacion.setEndValue(extend)
        self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animacion.start()

        print( vi, ' <> ',extend)
        print('ra: ',self.siz1, ' & ',self.sizx)
        print('ga: ',self.siz2, ' & ',self.sizy)
        #print(vi)

    def update_data(self):
        if(self.ui.frame_barra_menu.size().width()!=0):
            self.siz1=self.ui.frame_barra_menu.size().width()
        if(self.ui.frame_barra_tool.size().width()!=0):
            self.siz2=self.ui.frame_barra_tool.size().width()
        if(self.ui.frame_barra_menu.size().height()!=0):
            self.sizx=self.ui.frame_barra_menu.size().height()
        if(self.ui.frame_barra_tool.size().height()!=0):
            self.sizy=self.ui.frame_barra_tool.size().height()
	

    def rest_window(self): 
        self.showNormal()		
        self.ui.boto_restaurar.hide()
        self.ui.boto_max.show()
        self.update_data()


    def maxi_window(self): 
        self.showMaximized()
        self.ui.boto_max.hide()
        self.ui.boto_restaurar.show()
        self.update_data()

    def obtener_coordenada(self, event):
        x= event.pos().x()
        y= event.pos().y()
        print(x," |-| " ,y)

        doty= QPainter(self.ui.page)
        
        print(self.ui.page.isWidgetType())
        doty.begin(self.ui.page)

        doty.setPen(Qt.white)
        doty.drawRect(x, y, y, x)
        return x, y



if __name__== '__main__':
    print('raaaa')
    app= QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_cyan.xml')
    window= MainWindow()
    sys.exit(app.exec_())

