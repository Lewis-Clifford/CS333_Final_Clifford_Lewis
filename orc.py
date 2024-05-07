#Orc Class
#Inherits from Character class

from character import Character
from sword import Sword

class Orc(Character):
	#Constructor for orc
	def __init__(self, name="", health=0, equipped=Sword()):
		Character.__init__(self, name, health, equipped)

	#toString method
	def __str__(self):
		if self.equipped.getDamage() == 0:
			return self.name + ": " + str(self.health)
		else:
			return self.name + ": " + str(self.health) + "\n" + str(self.equipped)