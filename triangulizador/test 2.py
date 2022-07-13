from PyQt5 import QtCore, QtGui, QtWidgets


class TankWidget(QtWidgets.QWidget):
    progressChanged = QtCore.pyqtSignal(float)

    def __init__(self, parent=None):
        super().__init__(parent)

        self._progress = 0.0

    @QtCore.pyqtProperty(float, notify=progressChanged)
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, p):
        if 0 <= p <= 1.0:
            self._progress = p
            self.progressChanged.emit(p)
            self.update()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        height = self.progress * self.height()

        r = QtCore.QRect(0, self.height() - height, self.width(), height)
        painter.fillRect(r, QtGui.QBrush(QtCore.Qt.blue))
        pen = QtGui.QPen(QtGui.QColor("red"), 10)
        painter.setPen(pen)
        painter.drawRect(self.rect())

    def sizeHint(self):
        return QtCore.QSize(99, 99)


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 500)
        self.setWindowTitle("GUI 2.0")

        self.tank = TankWidget()
        self.progressbar = QtWidgets.QProgressBar()
        self.lcd = QtWidgets.QLCDNumber()
        self.lcd.setFixedHeight(99)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, maximum=100)
        self.button = QtWidgets.QPushButton("Button")

        self.slider.valueChanged.connect(self.on_value_changed)

        lay = QtWidgets.QGridLayout(self)
        lay.addWidget(self.tank, 0, 0, 2, 1)
        lay.addWidget(QtWidgets.QLabel("Tank", alignment=QtCore.Qt.AlignCenter), 2, 0)
        lay.addWidget(self.progressbar, 0, 1)
        lay.addWidget(self.lcd, 1, 1)
        lay.addWidget(self.slider, 2, 1)
        lay.addWidget(
            QtWidgets.QLabel(
                pixmap=QtGui.QPixmap("warning.png"), alignment=QtCore.Qt.AlignCenter
            ),
            0,
            2,
            2,
            1,
        )
        lay.addWidget(self.button, 2, 2)

        self.setFixedHeight(self.sizeHint().height())

        self.slider.setValue(40)

    @QtCore.pyqtSlot()
    def on_value_changed(self):
        progress = self.slider.value() * 1.0 / self.slider.maximum()
        self.tank.progress = progress
        self.progressbar.setValue(self.slider.value())
        self.lcd.display(self.slider.value())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())