
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

        self.my_groupbox = QExtendedGroupBox.ExtendedQGroupBox(self)

        self.myImage = QtGui.QPixmap("rotunda.jpg")
        self.myImage = self.myImage.scaled(self.myImage.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        hbox = QtGui.QHBoxLayout()

        self.my_label = QtGui.QLabel()
        self.my_label.setPixmap(self.myImage)
        
        self.my_label2 = QExtendedLabel.ExtendedQLabel(self.my_groupbox)
        hbox.addWidget(self.my_label) 
        hbox.addWidget(self.my_label2) 
        self.my_label2.setOriginalPixmap(self.myImage)
        self.my_label2.setMinimumSize(1, 1)

        self.rows = QtGui.QVBoxLayout()
        self.rows.addLayout(hbox)
        
        self.setLayout(self.rows) 
                

app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

