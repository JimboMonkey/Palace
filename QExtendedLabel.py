
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
        print "this card has an id of " + str(self.ID)
    
    def SetID(self, ID):
        self.ID = ID


#class ExtendedQLabel(QLabel):
#    def __init__(self, ID):
#        super(ExtendedQLabel, self).__init__()
#        self.ID = ID
  #  def __init__(self, id):
  #      super(AnotherTableWidgetItem, self).__init__()
  #      self.id = id


#class ExtendedQLabel(QLabel):

 #   def __init__(self, id):
  #      super(ExtendedQLabel, self).__init__()
   #     self.id = id




