
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
     
        self.Comp1TableCards = []
        self.Comp2TableCards = []
        self.PlayerTableCards = []
        self.Pile = []
        
        self.computer_cards = QExtendedGroupBox.ExtendedQGroupBox(self)
        self.dealer_cards = QExtendedGroupBox.ExtendedQGroupBox(self)
        self.player_cards = QExtendedGroupBox.ExtendedQGroupBox(self)      

        self.toprow = QtGui.QHBoxLayout()
        self.middlerow = QtGui.QHBoxLayout()
        self.bottomrow = QtGui.QHBoxLayout()


        self.toprow.addWidget(self.computer_cards)
        self.middlerow.addWidget(self.dealer_cards)
        self.bottomrow.addWidget(self.player_cards)

        self.rows = QtGui.QVBoxLayout()
        self.rows.addLayout(self.toprow)
        self.rows.addLayout(self.middlerow)
        self.rows.addLayout(self.bottomrow)

        
       # self.testlabel = QtGui.QLabel(self.computer_cards)
       # self.testlabel2 = QExtendedLabel.ExtendedQLabel(self.computer_cards)
       # for i in range(0, 3):
       #     self.my_label = QExtendedLabel.ExtendedQLabel(self.computer_cards)
        
        


        for i in range(0, 3):
            self.my_label = QExtendedLabel.ExtendedQLabel(self.computer_cards)
            #self.my_label2 = QExtendedLabel.ExtendedQLabel(self.my_label)
            self.my_label.setPixmap(self.myImage)
            #self.my_label2.setGeometry(50,50,50,50)
            #self.my_label2.show()
           # connect(self.computer_cards, SIGNAL(clicked()), this, SLOT(MakeConnections()));
            #self.my_label.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.MinimumExpanding)
            #self.my_label.setOriginalPixmap(self.myImage)
            #self.my_label.setMinimumSize(1, 1)
          
            #self.Comp1TableCards.append(self.my_label)
           # self.my_label.setPixmap(self.myImage.scaled(191, 250))
           # self.my_label.setScaledContents(True)
	
            #self.Comp1TableCards[i].setGeometry(200 + 195*i, 50, 191, 250)
            #self.Comp1TableCards[i].setOriginalPixmap(self.myImage)
            #self.Comp1TableCards[i].setMinimumSize(1, 1)
      
     #   self.my_label2 = QExtendedLabel.ExtendedQLabel(self.computer_cards)
            self.toprow.addWidget(self.my_label) 
            
     #   self.my_label2.setOriginalPixmap(self.myImage)
     #   self.my_label2.setMinimumSize(1, 1)

        self.PileSize = QExtendedLabel.ExtendedQLabel(self.dealer_cards)
        self.PileSize.setGeometry(1000, 0, 100, 50)
        self.PileSize.setText("")
        #self.computer_cards.jimjim()
        print "done"
        for i in xrange(0, 4):
            self.Pile.append(QExtendedLabel.ExtendedQLabel(self.dealer_cards))
            self.Pile[i].setOriginalPixmap(self.myImage)

            #self.Pile[i].setVisible(False)
            self.Pile[i].setMinimumSize(1, 1)
            if i < 3:
                self.Pile[i].setGeometry(1000, 40+i*60, 191, 250)
            else:
                self.Pile[i].setGeometry(1045, 40, 191, 250)  
        
        self.computer_cards.jimjim()
        self.setLayout(self.rows) 
        
        print "donevvvvvvvvvvv"
                

app = QtGui.QApplication([])
ex = Example()
ex.show()
sys.exit(app.exec_())

