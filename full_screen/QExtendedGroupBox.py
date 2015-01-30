
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import QExtendedLabel
from PyQt4 import QtGui
#from PyQt4.QtGui import QLabel

class ExtendedQGroupBox(QLabel):
    def __init__(self, parent):
        QGroupBox.__init__(self, parent)
        self.lineEditsList = []
#		super(AnotherTableWidgetItem, self).__init__()
 #       self.id = id
  
    def resizeEvent(self, ev):
#        QPixmap p; # load pixmap
        # get label dimensions
        print "hello", self.width(), self.height()
        #self.lineEditsList = self.findChildren(QExtendedLabel.ExtendedQLabel)
        #print len(self.lineEditsList)
        #if len(self.lineEditsList) > 0:
         #   print "boooo"
          #  self.myImage = QtGui.QPixmap("Mushroom.png")
           # self.lineEditsList[0].setPixmap(self.myImage)
            #self.lineEditsList[0].setGeometry(500,0,10000,5000)


    def jimjim(self):
        print self.items()
       # for item in lineEdits:
        #    self.lineEditsList.append(item)
        #
        #self.lineEditsList[0].setGeometry(500,0,10000,5000)





