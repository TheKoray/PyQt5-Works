# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 12:17:46 2021

@author: koray
"""

import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere()
        
    def pencere(self):
        
        self.setGeometry(200,200,500,500)
        self.setWindowTitle("Renk Değiştirme")
        self.setStyleSheet("background-color : yellow")
        
        self.buton = QtWidgets.QPushButton(self)
        self.buton.setText("BUTON")
        self.buton.move(200,200)
        self.buton.setStyleSheet("background-color : blue")
        self.buton.resize(50, 50)
        
        self.yazı_alanı = QtWidgets.QLabel(self)
        self.yazı_alanı.move(200,120)
        self.yazı_alanı.setText("YAZI ALANI")
        self.yazı_alanı.setStyleSheet("background-color : red")
        self.yazı_alanı.resize(70,50)
      
        self.show()

app = QtWidgets.QApplication(sys.argv)

pencere = Window()

sys.exit(app.exec_())