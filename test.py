
from Dealer import *
from Player import *
from Table import *

James = Player("James")
Phil = Player("Phil")

Table = Table()
Table.AddPlayer(James)
Table.AddPlayer(Phil)

#Table.ListPlayers()

Dealer = Dealer()
#Dealer.ListDeck()

for i in xrange(0, 3):
	for Player in Table.Players:
		Player.TakeCard(Dealer.DeckDeal())

for Player in Table.Players:
	Player.ListHand()


