
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from PyQt4.QtGui import QLabel

class ExtendedQLabel(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
#		super(AnotherTableWidgetItem, self).__init__()
 #       self.id = id
 
    def mouseReleaseEvent(self, ev):
        self.emit(SIGNAL('clicked()'))
        #print "this card has an id of " + str(self.ID)
    
    def SetID(self, ID):
        self.ID = ID

    def resizeEvent(self, ev):
#        QPixmap p; # load pixmap
        # get label dimensions
        print self.width(), self.height()

        # set a scaled pixmap to a w x h window keeping its aspect ratio 
 #       self.setPixmap(p.scaled(w,h,Qt::KeepAspectRatio);



