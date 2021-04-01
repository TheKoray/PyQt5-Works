# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:15:44 2021

@author: koray
"""
import os
import sys
from PyQt5 import QtWidgets


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.pencere()
        
    def pencere(self):
        
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("NotePad")
        
        self.yazı_alanı = QtWidgets.QTextEdit()
        
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Aç")
        self.kaydet = QtWidgets.QPushButton("Kaydet")
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazı_alanı)
        
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        
        self.show()
        
        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.yaziyi_ac)
        self.kaydet.clicked.connect(self.yaziyi_kaydet)
        
    def yaziyi_temizle(self):
        
        self.yazı_alanı.clear()
    
    def yaziyi_ac(self):
    
        dosya_ismi = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("Home"))
        
        with open(dosya_ismi[0],"r",encoding="utf-8") as file:
            
            self.yazı_alanı.setText(file.read())
        
    def yaziyi_kaydet(self):
        
        dosya_ismi = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("Home"))
        
        with open(dosya_ismi[0],"w") as file:
            
            file.write(self.yazı_alanı.toPlainText())
      
app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())



                                                                            






