#Shield Class
#Composite class for player class

class Shield():
	#Constructor for shield
	def __init__(self, name="", block=0):
		self.name = name
		self.block = block


	#getter for name
	def getName(self):
		return self.name
	
	#getter for block
	def getBlock(self):
		return self.block
	
	#setter for name
	def setName(self, name):
		self.name = name

	#setter for block
	def setBlock(self, block):
		self.block = block

	#toString method
	def __str__(self):
		return  self.name + " shield\n" + "Block: " + str(self.block)