# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:28:49 2021

@author: koray
"""

import sys 
from PyQt5 import QtWidgets

def Pencere():
    
    app = QtWidgets.QApplication(sys.argv)
    
    pencere = QtWidgets.QWidget() 
    pencere.setWindowTitle("İlk Pencere") 
    buton = QtWidgets.QPushButton(pencere)
    

    buton.setText("Yenile")
    buton.move(200,50)
    
    
    
    etiket = QtWidgets.QLabel(pencere) #ekrana yazı yazmak için etiket adında değişken tanımladık
    #etiket2 = QtWidgets.QLabel(Pencere)  #resim için etiket2 tanımladık
    #etiket2.setPixmap(QtGui.QPixmap("python.png"))   
    
    
    etiket.setText("Hello World")
    #etiket.setGeometry(20, 20, 500, 500) bu da yazıyı ekranda hareket ettirir
    etiket.move(210,30)
     
    pencere.setGeometry(100, 100, 500, 500)
    
    pencere.show()
    
    sys.exit(app.exec_())

Pencere()