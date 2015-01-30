
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

class ExtendedQPixmap(QtGui.QGraphicsPixmapItem):
    def __init__(self, parent):
        super(ExtendedQPixmap, self).__init__()

        #self.setPixmap(QtGui.QPixmap('craft.png'))
        #self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.state = 0
        #self.ID = 0
        

        #print "parent", parent.height()
 
    def mouseReleaseEvent(self, ev):
        #self.emit(SIGNAL('clicked()'))
#        print "this card has an id of " + str(self.ID)
        print "clicked " + str(self.ID)
    
    def setOrigPos(self, x, y):
        self.myx = x
        self.myy = y

    def getOrigX(self):
        return self.myx

    def getOrigY(self):
        return self.myy

    def SetID(self, ID):
        self.ID = ID
        self.setZValue(self.ID)

    def setOriginal(self, original):
        self.original = original
        self.setPixmap(self.original)

    def getOriginal(self):
        return self.original

    def setState(self, state):
        self.state = state

    def getState(self):
        return self.state


    def paintEvent(self,event):
        painter=QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.darkGray,3))
        painter.drawLine(self.startx,self.starty,self.endx,self.endy)
        painter.end()       
  




        
        


