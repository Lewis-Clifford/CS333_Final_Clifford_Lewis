#Driver for text adventure game

from character import Character
from player import Player
from orc import Orc
from sword import Sword
from shield import Shield

def main():
	fighter = Player()

	sword1 = Sword("Devilish Dicer", 8, 3)
	sword2 = Sword("Fingernail of Doom", 10, 5)
	shield = Shield("Wall of Ice", 6)
	orcSword = Sword("Hellfire Sword", 9, 4)
	orc = Orc("Bartholomew", 6, orcSword)

	playerName = input("What's your name? ")
	fighter.setName(playerName)
	fighter.setHealth(10)

	print("***Choose Your Own Adventure***\n")
	#Choice one
	print("You're walking through the woods and come upon a chest.\n Do you open it?\n")
	choiceOne = input("1. Yes\n2. No\n")

	result1 = firstChoice(choiceOne, fighter, sword1, sword2, shield)
	if result1 == 1:
		chooseSword(fighter, sword1, sword2)

	printStats(fighter)
	#Choice two
	print("As you pass a pond, you notice a bag on the ground.\n Do you open it?\n")
	choiceTwo = input("1. Yes\n2. No\n")

	secondChoice(choiceTwo, fighter, sword1, sword2, shield)

	printStats(fighter)
	#Choice three
	print("As you pass a rock, you see a sword sticking out of it.\n Do you pull it out?\n")
	choiceThree = input("1. Yes\n2. No\n")

	result3 = thirdChoice(choiceThree, fighter, sword1, sword2, shield)
	if result3 == 1:
		chooseSword(fighter, sword1, sword2)

	printStats(fighter)

	#Choice four
	print("A giant orc approaches! Do you fight or flee?\n")
	choiceFour = input("1. Fight\n2. Flee\n")

	fourthChoice(choiceFour, fighter, sword1, sword2, shield, orc)

	if fighter.getHealth() <= 0 and orc.getHealth() <= 0:
		print("You both die. Game over.\n")

	elif fighter.getHealth() <= 0:
		print("You die. Game over.\n")

	elif orc.getHealth() <= 0:
		print("You win! Congratulations!\n")

############################################################################################################

def printStats(character):
	print("Current Stats:\n" + str(character) + "\n")


############################################################################################################

def firstChoice(choiceOne, fighter, sword1, sword2, shield):
	valid = False
	while(valid == False):	
		if choiceOne == "1":
			valid = True
			print(sword1)
			fighter.insertSword(0, sword1)

			return 1



		elif choiceOne == "2":
			valid = True
			print("As you walk past the chest, you stub your toe and lose 1 HP.\n")
			fighter.setHealth(fighter.getHealth() - 1)
			return 2
		
		else:
			print("Invalid choice. Please choose again.\n")
			choiceOne = input("1. Yes\n2. No\n")

############################################################################################################

def secondChoice(choiceTwo, fighter, sword1, sword2, shield):
	valid = False
	while(valid == False):	
		if choiceTwo == "1":
			valid = True
			print(str(shield) + "\n")
			fighter.setShield(shield)

		elif choiceTwo == "2":
			valid = True
			print("While passing the pond, your foot gets wet and you eventually develop a blister. Lose 1 HP.\n")
			fighter.setHealth(fighter.getHealth() - 1)
		
		else:
			print("Invalid choice. Please choose again.\n")
			choiceTwo = input("1. Yes\n2. No\n")

############################################################################################################

def thirdChoice(choiceThree, fighter, sword1, sword2, shield):
	valid = False
	while(valid == False):	
		if choiceThree == "1":
			valid = True
			print(sword2)
			fighter.insertSword(len(fighter.swordList), sword2)

			return 1




		elif choiceThree == "2":
			valid = True
			print("While passing the rock, you stumble and scrape your knee. Lose 1 HP.\n")
			fighter.setHealth(fighter.getHealth() - 1)
			return 2

		else:
			print("Invalid choice. Please choose again.\n")
			choiceThree = input("1. Yes\n2. No\n")

############################################################################################################
#
def chooseSword(fighter, sword1, sword2):
	valid = False

	while(valid == False):
		print("Choose a sword:\n")
		print(fighter.getSwordList() + "\n")
		swordChoice = input()

		if swordChoice == "0":
			valid = True
			fighter.equipSword(0)
		elif swordChoice == "1" and len(fighter.swordList) > 1:
			valid = True
			fighter.equipSword(1)
		elif swordChoice == "1" and len(fighter.swordList) == 1:
			print("Invalid choice. Please choose again.\n")
		else:
			print("Invalid choice. Please choose again.\n")
	
############################################################################################################

def fourthChoice(choiceFour, fighter, sword1, sword2, shield, orc):
	valid = False
	while(valid == False):	
		if choiceFour == "1":
			valid = True
			fight(fighter, orc)
			return 1

		elif choiceFour == "2":
			valid = True
			print("As you turn to run, you trip on a log, and the orc steps on you. You die!\n")
			return 2
		else:
			print("Invalid choice. Please choose again.\n")
			choiceFour = input("1. Fight\n2. Flee\n")



############################################################################################################

def fight(fighter, orc):

	print(str(fighter) + "\n\n" + str(orc) + "\n")

	while(fighter.getHealth() > 0 and orc.getHealth() > 0):
		print(str(fighter) + "\n" + str(orc) + "\n")
		fh, oh = fightMath(fighter, orc)

	return fh, oh

############################################################################################################

def fightMath(fighter, orc):
	fighterDamage = fighter.getSword().getDamage()
	orcDamage = orc.getSword().getDamage()

	fighterBlock = max(fighter.getShield().getBlock(), fighter.getSword().getParryBlock())
	orcBlock = orc.getSword().getParryBlock()

	fighter.setHealth(fighter.getHealth() - (orcDamage - fighterBlock))
	orc.setHealth(orc.getHealth() - (fighterDamage - orcBlock))

	print("You take " + str(max(0, orcDamage - fighterBlock)) + " damage.\nThe orc takes " + str(max(0, fighterDamage - orcBlock)) + " damage.\n")
	return fighter.getHealth(), orc.getHealth()



if __name__ == "__main__":
	main()