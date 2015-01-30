#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ZetCode Advanced PyQt4 tutorial 

In this example, we demonstrate the nesting of 
layout managers. 

author: Jan Bodnar
website: zetcode.com 
last edited: October 2013
'''

import sys
from PyQt4 import QtGui, QtCore    
import QExtendedLabel

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.move(700, 700)
        self.setWindowTitle("Test")
       
        self.initUI()
        
        
    def initUI(self):
        self.myImage = QtGui.QPixmap("../Cards/CardBack.png")
        self.myImage = self.myImage.scaled(self.myImage.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)

        self.my_label = QExtendedLabel.ExtendedQLabel(self)
        hbox = QtGui.QHBoxLayout()    
        hbox.addWidget(self.my_label) 
        
        self.my_label.setOriginalPixmap(self.myImage)
         
        self.setLayout(hbox) 
                
app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())
