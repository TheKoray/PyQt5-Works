# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 23:39:08 2021

@author: koray
"""

import sys 
from PyQt5 import QtWidgets

def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("Buton Oluşturma")
    window.setGeometry(200, 200, 500, 500)
    
    buton = QtWidgets.QPushButton(window)
    buton.move(200, 150)
    buton.setText("Buton")
    
    window.show()
    
    sys.exit(app.exec_())
    
Window()

    
    
    