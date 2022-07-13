# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:49:50 2021

@author: UniverSapphireLotus
"""
#!/usr/bin/python
# Import all needed modules

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

# Create the Qt Application
app = QApplication(sys.argv)

# Create the root Widget/Window
window = QWidget()

# Create the Vertical Box Layout Manager, setting `window` as parent by passing it in the constructor.
layout = QVBoxLayout(window)

# Create and add the QPushButton Widgets to the `layout`
layout.addWidget(QPushButton('One'))
layout.addWidget(QPushButton('Two'))
layout.addWidget(QPushButton('Three'))
layout.addWidget(QPushButton('Four'))
layout.addWidget(QPushButton('Five'))

# Show the parent Widget
window.show()

# Run the main Qt loop and allow safe exiting
sys.exit(app.exec())