# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 00:16:32 2021

@author: koray
"""

import sys
from PyQt5 import QtWidgets 

def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("Vertical")
    window.setGeometry(200, 200, 500, 500)
    
    buton = QtWidgets.QPushButton(window)
    buton.setText("Buton")
    

    v_box = QtWidgets.QVBoxLayout(window)
    v_box.addWidget(buton)
    
    window.setLayout(v_box)
    
    window.show()
    
    sys.exit(app.exec_())
    
Window()