# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 01:15:16 2021

@author: koray
"""

import sys 
from PyQt5 import QtWidgets,QtGui

def Window():
    
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.setWindowTitle("Yazı Ve Resim Ekleme")
    window.setGeometry(100,100, 500, 500)
    
    yazı = QtWidgets.QLabel(window)
    
    yazı.setText("Pencereye Hoşgeldiniz")
    yazı.move(180,10) #Yazımızın Penceremizdeki konumunu belirttik
    
    resim = QtWidgets.QLabel(window)
    resim.setPixmap(QtGui.QPixmap("python.png"))
    resim.move(75, 125) #Resmimizin Penceremizdeki konumunu belirttik
    
    
    
    window.show()
    
    sys.exit(app.exec_())

    
Window()
    