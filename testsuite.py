#Unit tests for text adventure game

import unittest
import driver
from character import Character
from player import Player
from orc import Orc
from sword import Sword
from shield import Shield

class TestCharacter(unittest.TestCase):
	def test_getName_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(character.getName(), "Bob")

	def test_getHealth(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(character.getHealth(), 10)

	def test_setName_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.setName("Joe")
		self.assertEqual(character.getName(), "Joe")

	def test_setHealth_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.setHealth(5)
		self.assertEqual(character.getHealth(), 5)

	def test_setSword_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.setSword(Sword("New Sword", 7, 3))
		self.assertEqual(character.getSword().getName(), "New Sword")
		self.assertEqual(character.getSword().getDamage(), 7)
		self.assertEqual(character.getSword().getParryBlock(), 3)

	def test_getSword_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(character.getSword().getName(), "Sword")
		self.assertEqual(character.getSword().getDamage(), 5)
		self.assertEqual(character.getSword().getParryBlock(), 2)

	def test_insertSword_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.insertSword(0, Sword("New Sword", 7, 3))
		self.assertEqual(character.swordList[0].getName(), "New Sword")
		self.assertEqual(character.swordList[0].getDamage(), 7)
		self.assertEqual(character.swordList[0].getParryBlock(), 3)
	
	def test_equipSword_character(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.insertSword(0, Sword("New Sword", 7, 3))
		character.equipSword(0)
		self.assertEqual(character.getSword().getName(), "New Sword")
		self.assertEqual(character.getSword().getDamage(), 7)
		self.assertEqual(character.getSword().getParryBlock(), 3)

	def test_getSwordList(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		character.insertSword(0, Sword("New Sword", 7, 3))
		self.assertEqual(character.getSwordList(), "0: New Sword\n")

	def test_getSwordList_empty(self):
		character = Character("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(character.getSwordList(), "No swords in inventory")


	def test_getName_sword(self):
		sword = Sword("Sword", 5, 2)
		self.assertEqual(sword.getName(), "Sword")

	def test_getDamage_sword(self):
		sword = Sword("Sword", 5, 2)
		self.assertEqual(sword.getDamage(), 5)

	def test_getParryBlock_sword(self):
		sword = Sword("Sword", 5, 2)
		self.assertEqual(sword.getParryBlock(), 2)

	def test_setName_sword(self):
		sword = Sword("Sword", 5, 2)
		sword.setName("New Sword")
		self.assertEqual(sword.getName(), "New Sword")

	def test_setDamage_sword(self):
		sword = Sword("Sword", 5, 2)
		sword.setDamage(7)
		self.assertEqual(sword.getDamage(), 7)

	def test_setParryBlock_sword(self):
		sword = Sword("Sword", 5, 2)
		sword.setParryBlock(3)
		self.assertEqual(sword.getParryBlock(), 3)

	def test_str_sword(self):
		sword = Sword("Sword", 5, 2)
		self.assertEqual(str(sword), "Sword sword\nDamage: 5\nParry Block: 2")

	def test_getName_shield(self):
		shield = Shield("Shield", 5)
		self.assertEqual(shield.getName(), "Shield")

	def test_getBlock_shield(self):
		shield = Shield("Shield", 5)
		self.assertEqual(shield.getBlock(), 5)

	def test_setName_shield(self):
		shield = Shield("Shield", 5)
		shield.setName("New Shield")
		self.assertEqual(shield.getName(), "New Shield")

	def test_setBlock_shield(self):
		shield = Shield("Shield", 5)
		shield.setBlock(7)
		self.assertEqual(shield.getBlock(), 7)

	def test_str_shield(self):
		shield = Shield("Shield", 5)
		self.assertEqual(str(shield), "Shield shield\nBlock: 5")

	def test_getShield_player(self):
		player = Player("Bob", 10, Sword("Sword", 5, 2), Shield("Shield", 5))
		self.assertEqual(player.getShield().getName(), "Shield")
		self.assertEqual(player.getShield().getBlock(), 5)

	def test_setShield_player(self):
		player = Player("Bob", 10, Sword("Sword", 5, 2), Shield("Shield", 5))
		player.setShield(Shield("New Shield", 7))
		self.assertEqual(player.getShield().getName(), "New Shield")
		self.assertEqual(player.getShield().getBlock(), 7)

	def test_str_player(self):
		player = Player("Bob", 10, Sword("Sword", 5, 2), Shield("Shield", 5))
		self.assertEqual(str(player), "Bob: 10\nSword sword\nDamage: 5\nParry Block: 2\nShield shield\nBlock: 5")

	def test_str_orc(self):
		orc = Orc("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(str(orc), "Bob: 10\nSword sword\nDamage: 5\nParry Block: 2")

#Integration tests for interaction of modules with main driver

	def test_firstChoice_driver(self):
		player = Player("Bob", 10)
		sword1 = Sword("Devilish Dicer", 8, 3)
		sword2 = Sword("Fingernail of Doom", 10, 5)
		shield = Shield("Wall of Ice", 6)

		driver.firstChoice("1", player, sword1, sword2, shield)
		self.assertEqual(player.swordList[0].getName(), "Devilish Dicer")
		
		driver.firstChoice("2", player, sword1, sword2, shield)
		self.assertEqual(player.getHealth(), 9)

	def test_secondChoice_driver(self):
		player = Player("Alice", 10)
		sword1 = Sword("Devilish Dicer", 8, 3)
		sword2 = Sword("Fingernail of Doom", 10, 5)
		shield = Shield("Wall of Ice", 6)

		driver.secondChoice("1", player, sword1, sword2, shield)
		self.assertEqual(player.getShield().getName(), shield.getName())

		driver.secondChoice("2", player, sword1, sword2, shield)
		self.assertEqual(player.getHealth(), 9)

	def test_thirdChoice_driver(self):
		player = Player("Alice", 10)
		sword1 = Sword("Devilish Dicer", 8, 3)
		sword2 = Sword("Fingernail of Doom", 10, 5)
		shield = Shield("Wall of Ice", 6)

		driver.thirdChoice("1", player, sword1, sword2, shield)
		self.assertEqual(player.swordList[0].getName(), "Fingernail of Doom")

		driver.thirdChoice("2", player, sword1, sword2, shield)
		self.assertEqual(player.getHealth(), 9)

	def test_fourthChoice_driver(self):
		player = Player("Alice", 10)
		sword1 = Sword("Devilish Dicer", 8, 3)
		sword2 = Sword("Fingernail of Doom", 10, 5)
		shield = Shield("Wall of Ice", 6)
		orc = Orc("Bartholomew", 6, Sword("Hellfire Sword", 9, 4))

		
		self.assertEqual(driver.fourthChoice("1", player, sword1, sword2, shield, orc), 1)

		self.assertEqual(driver.fourthChoice("2", player, sword1, sword2, shield, orc), 2)

	def test_fight_driver(self):
		player = Player("Alice", 10, Sword("Sword", 5, 2))
		orc = Orc("Bartholomew", 6, Sword("Hellfire Sword", 9, 4))


		self.assertEqual(driver.fight(player, orc), (-4, 4)) #Tests integration of fightMath function also

	def test_fightMath_driver(self):
		player = Player("Alice", 10, Sword("Sword", 5, 2))
		orc = Orc("Bartholomew", 6, Sword("Hellfire Sword", 9, 4))

		self.assertEqual(driver.fightMath(player, orc), (3, 5))

#Integration tests for relationships between classes

	def test_player_relationships(self): #Tests relationships between player, character, sword, and shield
		player = Player("Alice", 10, Sword("Sword", 5, 2), Shield("Shield", 5))
		self.assertEqual(player.getName(), "Alice")
		self.assertEqual(player.getHealth(), 10)
		self.assertEqual(player.getSword().getName(), "Sword")
		self.assertEqual(player.getSword().getDamage(), 5)
		self.assertEqual(player.getSword().getParryBlock(), 2)
		self.assertEqual(player.getShield().getName(), "Shield")
		self.assertEqual(player.getShield().getBlock(), 5)

	def test_orc_relationships(self): #Tests relationships between orc, character, and sword
		orc = Orc("Bob", 10, Sword("Sword", 5, 2))
		self.assertEqual(orc.getName(), "Bob")
		self.assertEqual(orc.getHealth(), 10)
		self.assertEqual(orc.getSword().getName(), "Sword")
		self.assertEqual(orc.getSword().getDamage(), 5)
		self.assertEqual(orc.getSword().getParryBlock(), 2)

	def test_character_relationships(self): #Tests relationships between character and sword
		character = Character("Alice", 10, Sword("Sword", 5, 2))
		self.assertEqual(character.getName(), "Alice")
		self.assertEqual(character.getHealth(), 10)
		self.assertEqual(character.getSword().getName(), "Sword")
		self.assertEqual(character.getSword().getDamage(), 5)
		self.assertEqual(character.getSword().getParryBlock(), 2)
		
	

if __name__ == '__main__':
	unittest.main()