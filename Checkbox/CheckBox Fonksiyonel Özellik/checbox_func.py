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
        self.setWindowTitle("Checkbox Fonksiyonel Özellik")
        
        self.buton = QtWidgets.QPushButton(self)
        self.buton.setText("Buton")
        self.buton.move(200, 200)
        
        self.box_yes = QtWidgets.QCheckBox(self)
        self.box_yes.setText("Yes")
        self.box_yes.move(180, 140)
        
        self.box_no = QtWidgets.QCheckBox(self)
        self.box_no.setText("No")
        self.box_no.move(270,140)

        self.show()
        
        self.buton.clicked.connect(lambda : self.tikla(self.box_yes.isChecked(),self.box_no.isChecked()))
    
    def tikla(self,box_yes,box_no):
        
        if box_yes:
            
            print("Yes CheckBox'ı İşaretlendi")
        
        if box_no:
            
            print("No CheckBox'ı İşaretlendi")
        
        
        
        
        


app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())

