# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 22:08:59 2021

@author: koray
"""

import sys
from PyQt5 import QtWidgets

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere()
        
    def pencere(self):
        
        self.setGeometry(200,200,500, 500)
        self.setWindowTitle("RadioButton")
        
        self.radio_button = QtWidgets.QRadioButton(self)
        self.radio_button.setText("Yes")
        self.radio_button.move(180,180)
        
        self.radio_button1 = QtWidgets.QRadioButton(self)
        self.radio_button1.setText("No")
        self.radio_button1.move(250,180)
        
        
        self.show()
        

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())

        
        
        
        