
from __future__ import division
from collections import Counter
from Participant import *

class ComputerPlayer(Participant):
	def __init__(self, Name):
		Participant.__init__(self)
		self.Name = Name
		self.CardsToPlay = []

	def ListHand(self):
		print "\n" + self.Name + " is holding:"
		for Card in self.Hand:
			print "    " + Card.Name + " of " + Card.Suit
		print "    (" + str(self.HandScore()) + ")"
		#self.DecideCard()

	def HandValue(self):
		HandValue = 0
		for Card in self.Hand:
			HandValue += Card.Value
		return HandValue

	def HandScore(self):
		HandScore = self.HandValue() / len(self.Hand)
		return HandScore
	
	def DecideCard(self, PlayCardValue):
		self.ListHand()
		self.CardsToPlay = []
		CurrentHandValue = self.HandValue()
		CurrentNumberCards = len(self.Hand)
		#[y for y in x if y == 2]
		print "Playable cards:"
		if (PlayCardValue == 7):
			PlayableCards = [y.Value for y in self.Hand if y.Value <= PlayCardValue]
		else:
			PlayableCards = [y.Value for y in self.Hand if y.Value >= PlayCardValue]

		print PlayableCards

		if len(PlayableCards) == 0:
			print "can't play!"
			return None

		print ""
		CardValues = [i.Value for i in self.Hand]
		OccValues = [self.Hand.count(Val) for Val in CardValues]

		print "****************************"
		BestScore = 0
		Values = range(2,15)
		my_dict = Counter(PlayableCards)
	#	for i in my_dict:
		#	print str(i) + " = " + str(my_dict[i])
		for key in my_dict:
			#print str(key) + ":"
			for multiply in range(1,my_dict[key] + 1):
				#print "   " + str(key * multiply)
				PotentialHandValue = CurrentHandValue - (key * multiply)
				if PotentialHandValue == 0:
					PotentialHandValue = 1000
				else:
					PotentialHandScore = PotentialHandValue / (len(self.Hand) - multiply)
				print "If " + self.Name + " played " + str(multiply) + " " + str(key) + "'s his hand score would become " + str(PotentialHandScore)
				if (PotentialHandScore > BestScore):
					BestScore = PotentialHandScore
					BestMultiply = multiply
					BestValue = key
		print "****************************"

		print "The best score is " + str(BestScore)
		for i in range(0, BestMultiply):
			for Card in self.Hand:
				if Card.Value == BestValue:
					print "Playing the " + Card.Name + " of " + Card.Suit
					self.CardsToPlay.append(Card)
					self.Hand.remove(Card)
					break

		return self.CardsToPlay




