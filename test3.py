
#!/usr/bin/python

import sys
import QExtendedLabel
from functools import partial
from PyQt4 import QtGui, QtCore

from Dealer import *
from Player import *
from ComputerPlayer import *
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
		self.SelectedID = []
		self.Pile = []
		posXPlayer = 0
		grid = QtGui.QGridLayout()

		j = 0

		self.myImage = QtGui.QPixmap("Cards/CardBack.png")

		for i in xrange(0, 13):
			posYPlayer = 400
			posXPlayer += 45    
			for j in xrange(0, 4):
				element = ((i*4)+j)
				#print str(element)
				posYPlayer += 60
				self.CardHand.append(0)
				#self.PlayersHand.append(QExtendedLabel.ExtendedQLabel(element))
				self.PlayersHand.append(QExtendedLabel.ExtendedQLabel(self))
				self.connect(self.PlayersHand[element], QtCore.SIGNAL('clicked()'), partial(self.myDraw, element))	
				self.PlayersHand[element].setGeometry(posXPlayer, posYPlayer, 191, 250)
				self.PlayersHand[element].setVisible(False)
				self.PlayersHand[element].SetID(element)

		for i in xrange(0, 4):
			self.Pile.append(QExtendedLabel.ExtendedQLabel(self))
			#self.Pile[i].setPixmap(self.myImage)
			self.Pile[i].setVisible(False)
			if i < 3:
				self.Pile[i].setGeometry(20, 30+i*60, 191, 250)
			else:
				self.Pile[i].setGeometry(65, 30, 191, 250)

		self.Deck = QExtendedLabel.ExtendedQLabel(self)
		self.Deck.setGeometry(600, 50, 191, 250)
		self.Deck.setPixmap(self.myImage)

		self.GameStatus = QtGui.QLabel(self)
		font = QtGui.QFont('Serif', 16, QtGui.QFont.Light)
		self.GameStatus.setFont(font)
		self.GameStatus.setGeometry(300, 100, 500, 100)
		
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
		Phil = ComputerPlayer("Phil")
		Nash = ComputerPlayer("Nash")

		self.MyTable = Table()
		self.MyTable.AddPlayer(James)
		self.MyTable.AddPlayer(Phil)
		self.MyTable.AddPlayer(Nash)

		#MyTable.ListPlayers()

		self.MyDealer = Dealer()
		#self.MyDealer.ListDeck()

		for i in xrange(0, 3):
			for xPlayer in self.MyTable.Players:
				xPlayer.TakeCard(self.MyDealer.DeckDeal())

		for xPlayer in self.MyTable.Players:
			xPlayer.ListHand()
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


		self.move(300, 300)
		self.setGeometry(300, 100, 850, 900)
		self.setWindowTitle('Shithead')
		self.show()  



	def myDraw(self, element):
		cardID = self.PlayersHand[element].ID
##### From here all () element were swapped for cardID #####
		if(self.SelectedList.count(element) > 0):
			# Already selected so deselect
			#print str(element) + " deselected"
			# Remove from selection list
			self.SelectedList.remove(element)
			self.SelectedID.remove(cardID)
			self.UpdateHand()
		else:
			# Already deslected so select
			#print str(element) + " selected"
			# Add from selection list
			self.SelectedList.append(element)
			self.SelectedID.append(cardID)
			###############################################################
			# Check that only cards of the same value are selected
			res = len(set([x/4 for x in self.SelectedList]))
			# If not, clear all check boxes and the selection list
			if res > 1:
				for i in xrange(0, 52):
					del self.SelectedList[:]
					del self.SelectedID[:]
				self.SelectedList.append(element)
				self.SelectedID.append(cardID)
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

		#self.MyTable.Players[0].ListHand()

		for i in xrange(0, 52):
			self.PlayersHand[i].setVisible(False)

		sum = 0
		#del self.SelectedList[:]
#		print "Cards In players hand:"
		for card in self.MyTable.Players[0].Hand:
			self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
			#print "Loading card with ID of " + str(card.ID)
			if(card.Value != stored_val):
				card_num = (card_count * 4)
				card_count += 1
			else:
				card_num += 1

			self.PlayersHand[card_num].setEnabled(True)
			stored_val = card.Value
			#print self.SelectedList
			if self.SelectedList.count(card_num) > 0:
				MyRect = self.myImage.rect()
				self.qp = QtGui.QPainter()
				self.qp.begin(self.myImage)  
				self.drawLines(self.qp, MyRect)
				self.qp.end()
				#self.SelectedList.append(card_num)
			self.PlayersHand[card_num].setPixmap(self.myImage)
			self.PlayersHand[card_num].setVisible(True)
			self.PlayersHand[card_num].SetID(card.ID)
			
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

			sum += self.PlayersHand[card_num].isEnabled()

		if sum == 0:
			print "PICK UP!"
			self.GameStatus.setText("James picks up!")
			self.MyTable.Players[0].TakePile(self.MyDealer.PassPile())
			self.UpdateHand()
			self.UpdatePile([])
			
	def buttonClicked(self):
		self.play_list = []
		self.GameStatus.setText("")
		self.MyDealer.AddToPile(self.MyTable.Players[0].PlayCards(self.SelectedID))

		self.MyDealer.ListPile()
		self.SelectedList = []
		self.SelectedID = []
		NumberCards = len(self.MyTable.Players[0].Hand)
		if NumberCards < 3:
			for i in range(0, (3 - NumberCards)):
				self.MyTable.Players[0].TakeCard(self.MyDealer.DeckDeal())
		self.UpdateHand()
		self.PlayCardsButton.setVisible(False)
		self.UpdatePile(self.MyDealer.StatePile())

		##################################
		ComputersCards = self.MyTable.Players[1].DecideCard(self.MyDealer.PlayCardValue)
		if ComputersCards == None:
			self.MyTable.Players[1].TakePile(self.MyDealer.PassPile())
			self.UpdatePile([])
			self.GameStatus.setText("Virtual Phil picks up!")
		else:
			self.MyDealer.AddToPile(ComputersCards)
			NumberCards = len(self.MyTable.Players[1].Hand)
			if NumberCards < 3:
				for i in range(0, (3 - NumberCards)):
					self.MyTable.Players[1].TakeCard(self.MyDealer.DeckDeal())
			self.UpdatePile(self.MyDealer.StatePile())
		# Don't update here e;se you will pick up inbetween goes!!!!
		#self.UpdateHand()

		#################################
		ComputersCards = self.MyTable.Players[2].DecideCard(self.MyDealer.PlayCardValue)
		if ComputersCards == None:
			self.MyTable.Players[2].TakePile(self.MyDealer.PassPile())
			self.UpdatePile([])
			self.GameStatus.setText("Virtual Nash picks up!")
		else:
			self.MyDealer.AddToPile(ComputersCards)
			NumberCards = len(self.MyTable.Players[2].Hand)
			if NumberCards < 3:
				for i in range(0, (3 - NumberCards)):
					self.MyTable.Players[2].TakeCard(self.MyDealer.DeckDeal())
			self.UpdatePile(self.MyDealer.StatePile())
		self.UpdateHand()
		##################################		


				


	def UpdatePile(self, PileCards):
		i = 0
		if len(PileCards[-4:]) == 0:
			for i in xrange(0, 4):
				self.Pile[i].setVisible(False)		
		else:
			for Card in PileCards[-4:]:
				self.myImage = QtGui.QPixmap("Cards/" + Card.Name + Card.Suit + ".png")
				self.Pile[i].setPixmap(self.myImage)
				self.Pile[i].setVisible(True)
				i+=1
	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

