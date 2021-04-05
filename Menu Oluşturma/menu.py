# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 00:21:31 2021

@author: koray
"""

import sys 
from PyQt5.QtWidgets import QMainWindow,QApplication

class Window(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        
        menubar = self.menuBar()
        
        dosya = menubar.addMenu("Dosya")
        
        düzenle = menubar.addMenu("Düzenle")
        
        self.setWindowTitle("Menu Oluşturma")
        
        self.setGeometry(200, 200, 500, 500)
        
        self.show()
        
        
app = QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())