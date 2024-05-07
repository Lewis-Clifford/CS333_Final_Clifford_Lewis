#Player Class
#Inherits from Character class
#Composite class for shield class

from character import Character
from sword import Sword
from shield import Shield

class Player(Character):
	#Constructor for player
	def __init__(self, name="", health=0, equipped=Sword(), shield=Shield()):
		Character.__init__(self, name, health, equipped)
		self.shield = shield
		self.setShield(shield)


	#setter for shield
	def setShield(self, newShield):
		self.shield.setName(newShield.getName())
		self.shield.setBlock(newShield.getBlock())

	#getter for shield
	def getShield(self):
		return self.shield


	#toString method
	def __str__(self):
		if self.shield.getBlock() == 0 and self.equipped.getDamage() == 0:
			return self.name + ": " + str(self.health)
		
		elif self.shield.getBlock() == 0:
			return self.name + ": " + str(self.health) + "\n" + str(self.equipped)
		
		elif self.equipped.getDamage() == 0:
			return self.name + ": " + str(self.health) + "\n" + str(self.shield)
			
		else:
			return self.name + ": " + str(self.health) + "\n" + str(self.equipped) + "\n" + str(self.shield)