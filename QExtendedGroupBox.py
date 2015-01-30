
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#from PyQt4.QtGui import QLabel

class ExtendedQGroupBox(QLabel):
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
#		super(AnotherTableWidgetItem, self).__init__()
 #       self.id = id
  
    def resizeEvent(self, ev):
#        QPixmap p; # load pixmap
        # get label dimensions
        print "hello", self.width(), self.height()




