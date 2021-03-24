# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 22:44:40 2021

@author: koray
"""

import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere()
        
    def pencere(self):
        
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("TextEdit")
        
        self.yazı_alanı = QtWidgets.QTextEdit(self)
        
        self.yazı_alanı.move(50,100)
        self.yazı_alanı.resize(400,200)
        
        
        
        self.show()
        
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())