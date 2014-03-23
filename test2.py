
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
		self.PlayersHand = {}
		posXPlayer = 0
		self.MySelected = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
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
				self.PlayersHand[element] = QExtendedLabel.ExtendedQLabel(self)
				#self.connect(self.PlayersHand[element], QtCore.SIGNAL('clicked()'), self.myDraw)
				self.connect(self.PlayersHand[element], QtCore.SIGNAL('clicked()'), partial(self.myDraw, element))	
				self.PlayersHand[element].setGeometry(posXPlayer, posYPlayer, 191, 250)
				#self.PlayersHand[element].setPixmap(self.myImage)
				self.PlayersHand[element].setVisible(False)
				#print str(element) + " = " + str(element / 4) + " " + str(element % 4)
				self.MySelected[element/4][element%4] = 0
				self.checkbox[element] = QtGui.QCheckBox(str(element))
				#self.connect(self.checkbox[element], QtCore.SIGNAL('stateChanged()'), self.SelectionUpdate)	
				#self.checkbox[element].stateChanged.connect(partial (self.SelectionUpdate, element))
				grid.addWidget(self.checkbox[element], j, i)

		vBox = QtGui.QVBoxLayout()
		vBox.addWidget(PlayersCards)    

		#        self.setLayout(grid)   
		vBox.addLayout(grid)
		self.setLayout(vBox)

		James = Player("James")
		Phil = Player("Phil")

		self.MyTable = Table()
		self.MyTable.AddPlayer(James)
		self.MyTable.AddPlayer(Phil)

		#MyTable.ListPlayers()

		MyDealer = Dealer()
		#Dealer.ListDeck()

		for i in xrange(0, 3):
			for xPlayer in self.MyTable.Players:
				xPlayer.TakeCard(MyDealer.DeckDeal())

	#	for xPlayer in MyTable.Players:
#			xPlayer.ListHand()
		card_num = 0
		stored_val = 0
		card_count = 0
 		for card in xPlayer.Hand:
			self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
			print card.Value
			if(card.Value != stored_val):
				card_num = (card_count * 4)
				card_count += 1
			else:
				card_num += 1
			stored_val = card.Value
			self.PlayersHand[card_num].setPixmap(self.myImage)
			self.PlayersHand[card_num].setVisible(True)
		

			
		self.UpdateHand()	



		self.move(300, 200)
		self.setGeometry(300, 300, 850, 630)
		self.setWindowTitle('Shithead')
		self.show()  

	def myDraw(self, element):
		SelectedState = self.MySelected[element/4][element%4]
		if(SelectedState == 1):
			# Already selected so deselect
			print str(element) + " deselect"
			# Remove from selection list
			self.MySelected[element/4][element%4] = 0
			# Uncheck checkbox
			self.checkbox[element].setChecked(False)
			'''#self.myImage = QtGui.QPixmap("Cards/AceDiamonds.png")
			#self.PlayersHand[element].setPixmap(self.myImage)
			#############################################
			card_num = 0
			stored_val = 0
			card_count = 0
	 		for card in self.MyTable.Players[0].Hand:
				self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
				print card.Value
				if(card.Value != stored_val):
					card_num = (card_count * 4)
					card_count += 1
				else:
					card_num += 1
				stored_val = card.Value
				print "selected = " + str(self.MySelected[element/4][element%4])
				self.PlayersHand[card_num].setPixmap(self.myImage)
				self.PlayersHand[card_num].setVisible(True)

				#print self.PlayersHand[card_num].pixmap()
			#############################################
			#self.MySelected[element/4][element%4] = 0'''
		else:
			# Already deslected so select
			print str(element) + " select"
			# Add from selection list
			self.MySelected[element/4][element%4] = 1
			# Check checkbox
			self.checkbox[element].setChecked(True)
		
			###############################################################
			# Check that only cards of the same value are selected
			big_list = []
			for i  in xrange(0, 13):
				big_list.append(sum(self.MySelected[0:][i]))
			
			res = sum(i > 0 for i in big_list)
			# If not, clear all check boxes and the selection list
			if res > 1:
				for i in xrange(0, 52):
					self.MySelected[i/4][i%4] = 0
					self.checkbox[i].setChecked(False)
				# Tick the newly selected checkbox and selection in list
				self.checkbox[element].setChecked(True)
				self.MySelected[element/4][element%4] = 1
			##############################################################
				card_num = 0
				stored_val = 0
				card_count = 0
		 		for card in self.MyTable.Players[0].Hand:
					self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
					print card.Value
					if(card.Value != stored_val):
						card_num = (card_count * 4)
						card_count += 1
					else:
						card_num += 1
					stored_val = card.Value
					self.PlayersHand[card_num].setPixmap(self.myImage)
					self.PlayersHand[card_num].setVisible(True)
					#print self.PlayersHand[card_num].pixmap()
				#############################################
				#for i in xrange(0, 52):
					#self.myImage = QtGui.QPixmap("Cards/AceDiamonds.png")
					#self.PlayersHand[i].setPixmap(self.myImage)
					#self.MySelected[i/4][i%4] = 0
					self.checkbox[i].setChecked(False)

				self.checkbox[element].setChecked(True)
				MyRect = self.myImage.rect()
				self.qp = QtGui.QPainter()
				self.qp.begin(self.myImage)  
				self.drawLines(self.qp, MyRect)
				self.qp.end()
				self.PlayersHand[element].setPixmap(self.myImage)
			#############################################
			else:
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
					if(card_num == element):
						print str(card_num) + " should be red"
						MyRect = self.myImage.rect()
						self.qp = QtGui.QPainter()
						self.qp.begin(self.myImage)  
						self.drawLines(self.qp, MyRect)
						self.qp.end()
				#self.PlayersHand[element].setPixmap(self.myImage)
					self.PlayersHand[card_num].setPixmap(self.myImage)
					self.PlayersHand[card_num].setVisible(True)
				
					#print self.PlayersHand[card_num].pixmap()
				#############################################
	#			self.MySelected[element/4][element%4] = 1'''



	def drawLines(self, qp, MyRect):
		  
		pen = QtGui.QPen(QtCore.Qt.red, 4, QtCore.Qt.SolidLine)
		qp.setPen(pen)
		qp.drawRect(QtCore.QRect(MyRect))

	def SelectionUpdate(self, state, element):
		print state
		self.MySelected[element/4][element%4] = state

	def UpdateHand(self):
		card_num = 0
		stored_val = 0
		card_count = 0
		print "Cards In players hand:"
		for card in self.MyTable.Players[0].Hand:
			self.myImage = QtGui.QPixmap("Cards/" + card.Name + card.Suit + ".png")
			print card.Value
			if(card.Value != stored_val):
				card_num = (card_count * 4)
				card_count += 1
			else:
				card_num += 1
			
			stored_val = card.Value
			if (self.MySelected[card_num/4][card_num%4] == 1):
				MyRect = self.myImage.rect()
				self.qp = QtGui.QPainter()
				self.qp.begin(self.myImage)  
				self.drawLines(self.qp, MyRect)
				self.qp.end()
			self.PlayersHand[card_num].setPixmap(self.myImage)
			self.PlayersHand[card_num].setVisible(True)
				

	
				

	

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

