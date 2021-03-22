# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 21:43:22 2021

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
        self.setWindowTitle("CheckBox")
        
        self.checkbox = QtWidgets.QCheckBox(self)
        self.checkbox.setText("Yes")
        self.checkbox.move(180,100)
        
        self.checkbox2 = QtWidgets.QCheckBox(self)
        self.checkbox2.setText("No")
        self.checkbox2.move(230,100)
        
        
        self.show()
        
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())