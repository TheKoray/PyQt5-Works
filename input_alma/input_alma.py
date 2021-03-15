# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 01:38:24 2021

@author: koray
"""

import sys 
from PyQt5 import QtWidgets

def window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()    
    window.setGeometry(200, 200, 500, 500)
    window.setWindowTitle("Input Alma")
    
    yazı = QtWidgets.QLabel(window)
    yazı.setText("Yazı Alanı")
    yazı.move(100,200)
    
    yazı_al = QtWidgets.QLineEdit(window)
    yazı_al.move(170,200)
  
    
    window.show()
    
    sys.exit(app.exec_())
    
window()