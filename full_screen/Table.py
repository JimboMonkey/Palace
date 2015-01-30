
class Table(object):
	def __init__(self):

		self.Players = []

	def GetPlayer(self, PlayerIndex):
		return self.Players[PlayerIndex]

	def CountPlayers(self):
		return len(self.Players)

	def AddPlayer(self, Player):
		self.Players.append(Player)

	def RemovePlayer(self, PlayerIndex):
		del self.Players[PlayerIndex]

	def ListPlayers(self):
		for Player in self.Players:
			print Player.Name

