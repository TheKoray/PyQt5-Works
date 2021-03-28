# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:53:53 2021

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
        self.setWindowTitle("RadioButton Fonksiyonel Özellik")
        
        self.buton = QtWidgets.QPushButton(self)
        self.buton.setText("Buton")
        self.buton.move(200, 200)
        
        self.radio_yes = QtWidgets.QRadioButton(self)
        self.radio_yes.setText("Yes")
        self.radio_yes.move(180, 140)
        
        self.radio_no = QtWidgets.QRadioButton(self)
        self.radio_no.setText("No")
        self.radio_no.move(270,140)

        self.show()
        
        self.buton.clicked.connect(lambda : self.tikla(self.radio_yes.isChecked(),self.radio_no.isChecked()))
    
    def tikla(self,box_yes,box_no):
        
        if box_yes:
            
            print("Yes RadioButton'u İşaretlendi")
        
        if box_no:
            
            print("No RadioButton'u İşaretlendi")

app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())

