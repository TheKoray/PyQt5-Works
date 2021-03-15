# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 01:26:55 2021

@author: koray
"""

import sys 
from PyQt5 import QtWidgets


def window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setGeometry(200, 200, 500, 500)
    window.setWindowTitle("Horizontal")
    
    buton = QtWidgets.QPushButton(window)
    buton.setText("Buton")
    
    h_box = QtWidgets.QHBoxLayout(window)
    h_box.addWidget(buton)
    
    window.setLayout(h_box)
    
    window.show()
    
    sys.exit(app.exec_())
    
window()