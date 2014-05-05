
from Participant import *

class Player(Participant):
	def __init__(self, Name):
		Participant.__init__(self)
		self.MyTestNumber = 12
		self.Name = Name

	def TestNum(self):
		return self.MyTestNumber


	

