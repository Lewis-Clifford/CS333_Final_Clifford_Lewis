#Character class
#Parent class for player and orc
from sword import Sword

class Character():
	#Constructor for character


	def __init__(self, name="", health=0, equipped=Sword()):
		self.name = name
		self.health = health
		self.equipped = equipped
		self.setSword(equipped)
		self.swordList = []


	#getter for name
	def getName(self):
		return self.name
	
	#getter for health
	def getHealth(self):
		return self.health
	
	#setter for name
	def setName(self, name):
		self.name = name

	#setter for health
	def setHealth(self, health):
		self.health = health

	#setter for sword
	def setSword(self, newSword):
		self.equipped.setName(newSword.getName())
		self.equipped.setDamage(newSword.getDamage())
		self.equipped.setParryBlock(newSword.getParryBlock())

	#getter for sword
	def getSword(self):
		return self.equipped
	
	def insertSword(self, position, sword):
		self.swordList.insert(position, sword)

	def equipSword(self, position):
		self.setSword(self.swordList[position])


	#toString method for swordList
	def getSwordList(self):
		listString = ""
		if len(self.swordList) == 0:
			return "No swords in inventory"
		else:
			for i in range(len(self.swordList)):
				listString = listString + (str(i) + ": " + str(self.swordList[i].getName()) + "\n")
		
		return listString

	