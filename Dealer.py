
from Card import *
from random import randint

class Dealer(object):
	def __init__(self):

		self.Suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
		self.Names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
		self.Values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

		self.Deck = []
		self.Pile = []
		self.TopCard = 0
		self.PlayCardValue = 1

		self.CreateDeck()
		self.Shuffle()

	def CreateDeck(self):
		for SuitNumber in xrange(0,4):
			for CardNumber in xrange(0,13):
				ShoePosition = (CardNumber + (SuitNumber * 13))
				self.Deck.append(Card(self.Suits[SuitNumber], self.Names[CardNumber], self.Values[CardNumber], ShoePosition))

	def DeckSize(self):
		return len(self.Deck)

	def PileSize(self):
		return len(self.Pile)

	def DeckDeal(self):
	    return self.Deck.pop();

	def PassPile(self):
		PileCopy = self.Pile
		self.Pile = []
		self.PlayCardValue = 1
		return PileCopy

	def AddToPile(self, CardsToAdd):
		self.Pile.extend(CardsToAdd)
		self.TopFourCards = [i.Value for i in self.Pile[-4:]]
		# Check if 10 or invasion played
		if(self.TopFourCards.count(10)):
			print "\nBurn!"
			self.Pile = []
		elif (len(self.Pile[-4:]) == 4) and (len(set(self.TopFourCards)) == 1):
			print "\nInvasion!"
			self.Pile = []

		if not self.Pile:
			# Pile empty
			self.PlayCardValue = 1
		else:
			# Pile has card
			if(self.Pile[-1].Value != 8):
				self.PlayCardValue = self.Pile[-1].Value

	def PlayCardValue(self):
		return PlayCardValue

	def Shuffle(self):

		self.DeckSize = 52	

		# Use the Fisher-Yates / Knuth algorithm to shuffle the shoe
		for CardNumber in xrange(self.DeckSize, 0, -1):
			# Generate a random between 1 and the available shoe size
			RandomNumber = randint(0, (CardNumber-1))

			# Pick out a random card
			TempStore = self.Deck[RandomNumber]

			# Shift all sequential cards down by one position to fill the gap
			for ShuffleNumber in range(RandomNumber, (self.DeckSize - 1)):
				self.Deck[ShuffleNumber] = self.Deck[ShuffleNumber + 1];

			# Place the chosen card at the end of the pack
			self.Deck[self.DeckSize - 1] = TempStore;        

	def StatePile(self):
		return self.Pile

	def ListDeck(self):
		for CardNumber in xrange(0, 52):
			print "Card number " + str(CardNumber+1) + " is the " + self.Deck[CardNumber].Name + " of " + self.Deck[CardNumber].Suit + " with a value of " + str(self.Deck[CardNumber].Value)

	def ListPile(self):
		print "\n\nThe pile contains:"
		for card in self.Pile:
			print "   " + card.Name + " of " + card.Suit
		print "\n   Play card value is: " + str(self.PlayCardValue)
        

