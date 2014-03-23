
#!/usr/bin/python

import sys
import QExtendedLabel
from functools import partial
from PyQt4 import QtGui, QtCore

from Dealer import *
from Player import *
from Table import *

class Example(QtGui.QWidget):
    
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()
        
	def initUI(self):      

		PlayersCards = 	QtGui.QGroupBox(self)
		self.PlayersHand = []
		self.CardHand = []
		self.SelectedList = []
		posXPlayer = 0
		self.checkbox = {}
		grid = QtGui.QGridLayout()

		j = 0
		pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]


		self.myImage = QtGui.QPixmap("Cards/AceDiamonds.png")

		for i in xrange(0, 13):
			posYPlayer = 0
			posXPlayer += 45    
			for j in xrange(0, 4):
				element = ((i*4)+j)
				#print str(element)
				posYPlayer += 60
				self.CardHand.append(0)
				self.PlayersHand.append(QExtendedLabel.ExtendedQLabel(self))
				self.connect(self.PlayersHand[element], QtCore.SIGNAL('clicked()'), partial(self.myDraw, element))	
				self.PlayersHand[element].setGeometry(posXPlayer, posYPlayer, 191, 250)
				self.PlayersHand[element].setVisible(False)
				self.checkbox[element] = QtGui.QCheckBox(str(element))
				grid.addWidget(self.checkbox[element], j, i)

		vBox = QtGui.QVBoxLayout()
		vBox.addWidget(PlayersCards)    

		#        self.setLayout(grid)   
		vBox.addLayout(grid)

		self.PlayCardsButton = QtGui.QPushButton("Play Cards", self)
		self.PlayCardsButton.setVisible(False)
		self.PlayCardsButton.clicked.connect(self.buttonClicked)  
		vBox.addWidget(self.PlayCardsButton)

		self.setLayout(vBox)

		James = Player("James")
		Phil = Player("Phil")

		self.MyTable = Table()
		self.MyTable.AddPlayer(James)
		self.MyTable.AddPlayer(Phil)

		#MyTable.ListPlayers()

		self.MyDealer = Dealer()
		#self.MyDealer.ListDeck()

		for i in xrange(0, 13):
			for xPlayer in self.MyTable.Players:
				xPlayer.TakeCard(self.MyDealer.DeckDeal())

	#	for xPlayer in MyTable.Players:
#			xPlayer.ListHand()
		card_num = 0
		stored_val = 0
		card_count = 0
 		for card in self.MyTable.Players[0].Hand:
			self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
			#print card.Value
			if(card.Value != stored_val):
				card_num = (card_count * 4)
				card_count += 1
			else:
				card_num += 1
			stored_val = card.Value
			self.PlayersHand[card_num].setPixmap(self.myImage)
			self.PlayersHand[card_num].setVisible(True)
			self.CardHand[card_num] = card			
			
		self.UpdateHand()


		self.move(300, 200)
		self.setGeometry(300, 300, 850, 630)
		self.setWindowTitle('Shithead')
		self.show()  

	def myDraw(self, element):
		if(self.SelectedList.count(element) > 0):
			# Already selected so deselect
			#print str(element) + " deselected"
			# Remove from selection list
			self.SelectedList.remove(element)
			# Uncheck checkbox
			self.checkbox[element].setChecked(False)
			self.UpdateHand()
		else:
			# Already deslected so select
			#print str(element) + " selected"
			# Add from selection list
			self.SelectedList.append(element)
			# Check checkbox
			self.checkbox[element].setChecked(True)
			###############################################################
			# Check that only cards of the same value are selected
			res = len(set([x/4 for x in self.SelectedList]))
			# If not, clear all check boxes and the selection list
			if res > 1:
				for i in xrange(0, 52):
					del self.SelectedList[:]
					self.checkbox[i].setChecked(False)
				# Tick the newly selected checkbox and selection in list
				self.checkbox[element].setChecked(True)
				self.SelectedList.append(element)
				##############################################################
			self.UpdateHand()
		#print self.SelectedList
		self.PlayCardsButton.setVisible(len(self.SelectedList))
		
			



	def drawLines(self, qp, MyRect):
		  
		pen = QtGui.QPen(QtCore.Qt.red, 4, QtCore.Qt.SolidLine)
		qp.setPen(pen)
		qp.drawRect(QtCore.QRect(MyRect))


	def UpdateHand(self):
		card_num = 0
		stored_val = 0
		card_count = 0
		#del self.SelectedList[:]
#		print "Cards In players hand:"
		for card in self.MyTable.Players[0].Hand:
			self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
			#print card.Value
			if(card.Value != stored_val):
				card_num = (card_count * 4)
				card_count += 1
			else:
				card_num += 1
			
			stored_val = card.Value
			if self.SelectedList.count(card_num) > 0:
				MyRect = self.myImage.rect()
				self.qp = QtGui.QPainter()
				self.qp.begin(self.myImage)  
				self.drawLines(self.qp, MyRect)
				self.qp.end()
				#self.SelectedList.append(card_num)
			self.PlayersHand[card_num].setPixmap(self.myImage)
			self.PlayersHand[card_num].setVisible(True)
			if(card.Value not in (2,8,10)):
				if(self.MyDealer.PlayCardValue == 7):
					if card.Value > self.MyDealer.PlayCardValue:
						self.PlayersHand[card_num].setEnabled(False)
					else:
						self.PlayersHand[card_num].setEnabled(True)
				else:
					if card.Value < self.MyDealer.PlayCardValue:
						self.PlayersHand[card_num].setEnabled(False)
					else:
						self.PlayersHand[card_num].setEnabled(True)
			
				
	def buttonClicked(self):
		print "\nPlaying the:"
		self.play_list = []
		for i in xrange(0, 52):
			if self.SelectedList.count(i) > 0:
				#print i
				print "   " + self.CardHand[i].Name + " of " + self.CardHand[i].Suit
		for index in self.SelectedList:
			self.play_list.append(self.CardHand[index])
		self.MyDealer.AddToPile(self.play_list)
		self.MyDealer.ListPile()
		self.UpdateHand()


	
				

	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

