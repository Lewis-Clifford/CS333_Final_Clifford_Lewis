#Sword class
#Composite with character class

class Sword():
	#Constructor for sword

	def __init__(self, name="", damage=0, parryBlock=0):
		self.name = name
		self.damage = damage
		self.parryBlock = parryBlock
	

	#getter for name
	def getName(self):
		return self.name
	
	#getter for damage
	def getDamage(self):
		return self.damage
	
	#getter for parryBlock
	def getParryBlock(self):
		return self.parryBlock
	
	#setter for name
	def setName(self, name):
		self.name = name

	#setter for damage
	def setDamage(self, damage):
		self.damage = damage

	#setter for parryBlock
	def setParryBlock(self, parryBlock):
		self.parryBlock = parryBlock

	#toString method
	def __str__(self):
		return  self.name + " sword\n" + "Damage: " + str(self.damage) + "\nParry Block: " + str(self.parryBlock)