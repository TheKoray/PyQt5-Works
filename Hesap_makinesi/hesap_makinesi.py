# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 00:11:48 2021

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
        self.setWindowTitle("ToplaÇıkar")
        
        self.buton_topla = QtWidgets.QPushButton("Topla")
        self.buton_çıkar = QtWidgets.QPushButton("Çıkar")
        self.yenile = QtWidgets.QPushButton("Yenile")
        self.yazı_alanı1 = QtWidgets.QLineEdit()
        
        self.yazı_alanı2 = QtWidgets.QLineEdit()
        
        
        self.sonuc = QtWidgets.QLabel()
        self.sonuc.setText("Sonuç")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.yazı_alanı1)
        v_box.addWidget(self.yazı_alanı2)
        v_box.addWidget(self.sonuc)
        
        v_box.addStretch()
        v_box.addWidget(self.yenile)
        v_box.addWidget(self.buton_topla)
        v_box.addWidget(self.buton_çıkar)
        
        self.setLayout(v_box)
        
        self.show()
        
        self.yenile.clicked.connect(self.yeni)
        self.buton_topla.clicked.connect(self.topla)
        self.buton_çıkar.clicked.connect(self.cikar)
        
    def yeni(self):
        
        self.yazı_alanı1.clear()
        self.yazı_alanı2.clear()
    
    def topla(self):
        
        self.result = int(self.yazı_alanı1.text()) + int(self.yazı_alanı2.text())
        self.sonuc.setText(str(self.result))
       
        
    def cikar(self):
        
        self.result = int(self.yazı_alanı1.text()) - int(self.yazı_alanı2.text())
        self.sonuc.setText(str(self.result))
        
app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())