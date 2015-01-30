
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui

class ExtendedQLabel(QtGui.QGraphicsPixmapItem):
    def __init__(self, parent):
        super(ExtendedQLabel, self).__init__()

        self.setPixmap(QtGui.QPixmap('craft.png'))
        #self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
        self.state = 0
 
    def mouseReleaseEvent(self, ev):
        #self.emit(SIGNAL('clicked()'))
#        print "this card has an id of " + str(self.ID)
        pass#print "clicked " + str(self.ID)
    
    def SetID(self, ID):
        self.ID = ID

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
  

    def resizeEvent(self, ev):
#        QPixmap p; # load pixmap
        # get label dimensions
        #print self.width(), self.height()
        print "label"

        # set a scaled pixmap to a w x h window keeping its aspect ratio 
        #self.setPixmap(p.scaled(w,h,Qt::KeepAspectRatio);
        self.setScaledPixmap()

    def setOriginalPixmap(self,pixmap):
        self.original_pixmap = pixmap
        #self.setPixmap(self.original_pixmap)
        self.setScaledPixmap()

    def setScaledPixmap(self):
        print self.width(), self.height()
        scaled_pixmap = self.original_pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.setPixmap(scaled_pixmap)


        
        


