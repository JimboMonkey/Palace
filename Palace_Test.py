import sys
from PyQt4 import QtGui, QtCore
import time
import random
import QExtendedLabel
import QExtendedGroupBox


class MyThread(QtCore.QThread):
    trigger = QtCore.pyqtSignal(int,int,int,int)

    def __init__(self, parent=None):
        super(MyThread, self).__init__(parent)

    def setup(self, thread_no):
        self.thread_no = thread_no

    def run(self):
        for i in range(0,10):
            time.sleep(random.random()*5)  # random sleep to imitate working
            self.trigger.emit(random.random()*10,random.random()*10,random.random()*10,random.random()*10)
		


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.myImage = QtGui.QPixmap("Cards/CardBack.png")
        self.myImage = self.myImage.scaled(self.myImage.size(), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
     
        self.Comp1TableCards = []
        self.Comp2TableCards = []
        self.PlayerTableCards = []
        self.Pile = []

        central_widget = QtGui.QWidget()

        self.computer_cards = QExtendedGroupBox.ExtendedQGroupBox(self)
        self.dealer_cards = QtGui.QGroupBox()
        self.player_cards = QtGui.QGroupBox()
 
        for i in range(0, 3):
            self.my_label = QExtendedLabel.ExtendedQLabel(self.computer_cards)
            self.my_label.setSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.MinimumExpanding)
            self.my_label.setOriginalPixmap(self.myImage)
            self.my_label.setMinimumSize(1, 1)
          
            self.Comp1TableCards.append(self.my_label)
           # self.my_label.setPixmap(self.myImage.scaled(191, 250))
           # self.my_label.setScaledContents(True)
	
            self.Comp1TableCards[i].setGeometry(200 + 195*i, 50, 191, 250)
            self.Comp1TableCards[i].setPixmap(self.myImage)

            self.Comp2TableCards.append(QExtendedLabel.ExtendedQLabel(self.computer_cards))
            self.Comp2TableCards[i].setGeometry(1100 + 195*i, 50, 191, 250)
            self.Comp2TableCards[i].setPixmap(self.myImage)

            self.PlayerTableCards.append(QExtendedLabel.ExtendedQLabel(self.player_cards))
            self.PlayerTableCards[i].setGeometry(700 + 195*i, 60, 191, 250)
            self.PlayerTableCards[i].setPixmap(self.myImage)

        for i in range(3, 6):
            self.Comp1TableCards.append(QExtendedLabel.ExtendedQLabel(self.computer_cards))
            self.Comp1TableCards[i].setGeometry(210 + 195*(i-3), 60, 191, 250)
            self.Comp1TableCards[i].setPixmap(self.myImage)

            self.Comp2TableCards.append(QExtendedLabel.ExtendedQLabel(self.computer_cards))
            self.Comp2TableCards[i].setGeometry(1110 + 195*(i-3), 60, 191, 250)
            self.Comp2TableCards[i].setPixmap(self.myImage)

            self.PlayerTableCards.append(QExtendedLabel.ExtendedQLabel(self.player_cards))
            self.PlayerTableCards[i].setGeometry(710 + 195*(i-3), 70, 191, 250)
            self.PlayerTableCards[i].setPixmap(self.myImage)

        self.toprow = QtGui.QHBoxLayout()
        self.middlerow = QtGui.QHBoxLayout()
        self.bottomrow = QtGui.QHBoxLayout()

        #self.Deck = QExtendedLabel.ExtendedQLabel(self.dealer_cards)
        #self.Deck.setGeometry(800, 40, 191, 250)
        #self.Deck.setPixmap(self.myImage)

        self.DeckSize = QtGui.QLabel(self.dealer_cards)
        self.DeckSize.setGeometry(800, 0, 100, 50)
        self.DeckSize.setText("")

        self.PileSize = QtGui.QLabel(self.dealer_cards)
        self.PileSize.setGeometry(1000, 0, 100, 50)
        self.PileSize.setText("")

        for i in xrange(0, 4):
            self.Pile.append(QExtendedLabel.ExtendedQLabel(self.dealer_cards))
            self.Pile[i].setPixmap(self.myImage)
            #self.Pile[i].setVisible(False)
            if i < 3:
                self.Pile[i].setGeometry(1000, 40+i*60, 191, 250)
            else:
                self.Pile[i].setGeometry(1045, 40, 191, 250)


        self.Comp1HandSize = QtGui.QLabel(self.computer_cards)
        self.Comp1HandSize.setGeometry(200, 10, 100, 50)
        self.Comp1HandSize.setText("")
        
        self.Comp2HandSize = QtGui.QLabel(self.computer_cards)
        self.Comp2HandSize.setGeometry(1100, 10, 100, 50)
        self.Comp2HandSize.setText("")

        self.toprow.addWidget(self.computer_cards)
        #self.toprow.addStretch()
        self.middlerow.addWidget(self.dealer_cards)
        self.bottomrow.addWidget(self.player_cards)

        self.rows = QtGui.QVBoxLayout()
        self.rows.addLayout(self.toprow)
        self.rows.addLayout(self.middlerow)
        self.rows.addLayout(self.bottomrow)

        self.big_layout = QtGui.QVBoxLayout()

        central_widget.setLayout(self.rows)


        self.my_button = QtGui.QPushButton('Start')
        self.my_button.clicked.connect(self.start_game_thread)
      #  central_layout.addWidget(self.my_button)
        
        self.myImage = QtGui.QPixmap("Mushroom.png")
        self.myImage2 = QtGui.QPixmap("ChainChomp.png")

      #  central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)
       # self.setCentralWidget(self.big_layout)
        self.start_game_thread()
     #   thread = MyThread(self)    # create a thread
    #    thread.trigger.connect(self.show_image)  # connect to it's signal

    def UpdateCardCounts(self, Comp1, Comp2, Deck, Pile):
        self.Comp1HandSize.setText('Phil has %d cards in his hand' % Comp1)
        self.Comp2HandSize.setText('Nash has %d cards in his hand' % Comp2)
        self.DeckSize.setText('The deck has %d cards left' % Deck)
        self.PileSize.setText('The pile contains %d cards' % Pile)

    def show_image(self, thread_no):
        if thread_no < 5:
	        self.my_pic.setPixmap(self.myImage)
        else:
	        self.my_pic.setPixmap(self.myImage2)


    def start_game_thread(self):
        thread = MyThread(self)    # create a thread
   #     thread.trigger.connect(self.show_image)  # connect to it's signal
        thread.trigger.connect(self.UpdateCardCounts)  # connect to it's signal
        thread.start()             # start the thread
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)

    mainwindow = Main()
    mainwindow.setGeometry(100, 100, 900, 600)
    #mainwindow.showMaximized()
    mainwindow.setWindowTitle('Testing')
    mainwindow.show()

    sys.exit(app.exec_())

