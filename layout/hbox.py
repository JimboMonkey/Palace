#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt4 tutorial 

This is a simple QHBoxLayout example.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2013
'''

import sys
from PyQt4 import QtGui
      
        
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.move(300, 300)
        self.setWindowTitle("QHBoxLayout")
       
        self.initUI()
        
        
    def initUI(self):
    
        btn1 = QtGui.QPushButton("Button", self)
        btn2 = QtGui.QPushButton("Button", self)
        btn3 = QtGui.QPushButton("Button", self)
        btn4 = QtGui.QPushButton("Button", self)
        
        layout = QtGui.QHBoxLayout()
        layout.addWidget(btn1) 
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        layout.addWidget(btn4)
        self.setLayout(layout) 
        

app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
