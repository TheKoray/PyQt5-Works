# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 00:45:31 2021

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
        self.setWindowTitle("Button Function")
        self.say = 0
        
        self.buton = QtWidgets.QPushButton("Buton")
        self.yazı_alanı = QtWidgets.QLineEdit()
        self.sonuc = QtWidgets.QLabel()
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.buton)
        v_box.addStretch()        
        
        self.setLayout(v_box)
        
        self.show()
        
        self.buton.clicked.connect(self.tikla)
        
    def tikla(self):
        
        self.sonuc.setText(self.yazı_alanı.text())
        self.yazı_alanı.clear()
          
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())


