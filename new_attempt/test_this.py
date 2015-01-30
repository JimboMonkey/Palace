
import sys
from PyQt4 import QtGui, QtCore    
import QExtendedLabel
import QExtendedGroupBox

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.move(300, 300)
        self.setWindowTitle("Resize Test")
       
        self.initUI()
        
        
    def initUI(self):
        self.myImage = QtGui.QPixmap("CardBack.png")
        self.myImage = self.myImage.scaled(self.myImage.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.mylayout = QtGui.QHBoxLayout()
        self.setLayout(self.mylayout)
 
        # lbl occupies whole frame
        self.my_label = QtGui.QLabel()
        self.my_label.setPixmap(self.myImage)
        self.mylayout.addWidget(self.my_label);
 
        # lbltop is the child of lbl
        self.my_label2 = QtGui.QLabel(self.my_label)
        self.my_label2.setPixmap(self.myImage)
        self.my_label2.setGeometry(50,50,50,50)
        self.my_label2.show()
 
app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())


