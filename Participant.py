
class Participant(object):
	def __init__(self):

		self.Hand = []
		self.Facedowns = []
		self.Faceups = []
		self.CardsToPlay = []

	def InitialTakeCard(self, CardToTake):
		print "\n" + self.Name + " taking a card"
		if len(self.Facedowns) < 3:
			self.Facedowns.append(CardToTake)
		else:
			self.Faceups.append(CardToTake)


	def TakeCard(self, CardToTake):
		self.Hand.append(CardToTake)
		self.SortHand()

	def ListHand(self):
		print "\n" + self.Name + " is holding in facedowns:"
		for Card in self.Facedowns:
			print "    " + Card.Name + " of " + Card.Suit
		print "\n" + self.Name + " is holding in faceups:"
		for Card in self.Faceups:
			print "    " + Card.Name + " of " + Card.Suit
		print "\n" + self.Name + " is holding in hand:"
		for Card in self.Hand:
			print "    " + Card.Name + " of " + Card.Suit

	def TakePile(self, Pile):
		self.Hand.extend(Pile)
		self.SortHand()
	
	def SortHand(self):
		self.Hand.sort(key=lambda Card: Card.Value)
		# Check for invasion potential

	def PlayCards(self, CardsToRemove):
		#for Card in CardsToRemove:
		#	print str(Card.Name) + " of " + str(Card.Suit) + " has an index of " + str(Card.ID)
		#	self.Hand.remove(Card)
		self.CardsToPlay = []
		print "removing " + str(CardsToRemove)
		for i in range(0,len(CardsToRemove)):
			for Card in self.Hand:
				for Index in CardsToRemove:
					if Card.ID == Index:
						self.CardsToPlay.append(Card)
						self.Hand.remove(Card)
		#				print "delete " + str(Card.Name) + " of " + str(Card.Suit)
		return self.CardsToPlay
        


#	def PlayCards(self):
#		TempCardsList = self.CardsToPlay
#		self.CardsToPlay = []
#		return TempCardsList


	def HandSize(self):
		return len(self.Hand)


