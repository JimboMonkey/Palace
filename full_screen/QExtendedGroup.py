
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MyGroup(QtGui.QGraphicsItemGroup):
    
    def __init__(self, name):
        super(MyGroup, self).__init__()
        
        self.setCursor(QtCore.Qt.OpenHandCursor)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, 
            True)
        self.name = name

    def getName(self):
        return self.name
    
    def paint(self, painter, option, widget):
    
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        
        brush = QtGui.QBrush(QtGui.QColor("#333333"))
        pen = QtGui.QPen(brush, 0.5)
        pen.setStyle(QtCore.Qt.DotLine)
        painter.setPen(pen)
        
        if self.isSelected():
            boundRect = self.boundingRect()
            painter.drawRect(boundRect) 

    def resizeEvent(self, ev):
        print "boo ya!"
