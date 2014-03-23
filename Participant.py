
class Participant(object):
	def __init__(self):

		self.Hand = []
		self.Facedowns = []
		self.Faceups = []
		self.CardsToPlay = []

	def TakeCard(self, CardToTake):
		self.Hand.append(CardToTake)
		self.SortHand()

	def TakePile(self, Pile):
		self.Hand.extend(Pile)
		self.SortHand()
	
	def SortHand(self):
		self.Hand.sort(key=lambda Card: Card.Value)
		# Check for invasion potential

	def PlayCards(self):
		return self.CardsToPlay

	def HandSize(self):
		return len(self.Hand)


