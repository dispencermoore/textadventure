import random
print ("\n Welcome to Spencer's Super Awesome Amazing Wonderful Text Adventure! \n");
print ("It is very simple. For every turn, you will input a command. In case you don't want to memorize the commands, just type 'Commands' whenever you want to know them all! For those of you with handy dandy memory, here is the *mostly full list. Move Forward (MF), Move Back (MB), Move Left (ML), Move Right (MR), Attack, Retreat, Inspect, LookAround (Which also tells you what you're carrying), PickUp. And that's all! Goodluck!");

roomsLayout = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
charInventory = []

startingRoomNumber = random.randint(0,24)
roomsLayout.remove(startingRoomNumber)
roomsLayout.insert(startingRoomNumber, 'startingRoom')
currentRoomNumber = startingRoomNumber
print (startingRoomNumber)
print (roomsLayout)

dangerRating = 0
fightTrue = 0
damageTaken = 0
healthMods = 0
weaponDamage = 0
monstersKilled = 0
characterBaseAttack = 2
characterAttack = characterBaseAttack + weaponDamage
currentHealth = 30 - damageTaken + healthMods
	
class Item():
	def __init__(self, name, description, value, health, damage):
		self.name = name
		self.description = description
		self.value = value
		self.health = health
"""weaponDamage = self.damage"""

class Room():
	def __init__(self, name, description, danger, loot):
		self.name = name
		self.description = description
		self.danger = danger
		self.loot = loot

class Monster():
	def __init__(self, name, description, health, damage):
		self.name = name
		self.description = description
		self.health = health
		self.damage = damage 
	
"""just a comment for how rooms work. There is a grid, each spot has a number. When you visit, the number will be assigned a room, so you can return to it. It is 5x5 
21 22 23 24 25
16 17 18 19 20  btw everything is shifted down one but im too lazy to fix the graph, just refer to the array
11 12 13 14 15
6  7  8  9  10
1  2  3  4  5
"""

registry = {}
	
spookyCorridor = Room('Spooky Corridor', 'It is a corridor. And it is spooky.', 6, 2)

auaojaj = Monster('An Unholy Abomination Of Jasper And Journey, or AUAOJAJ.', 'The monsters name says it all tbh.', 10, 3)

medusa = Monster('SSSSSSSamantha.', 'Snake lady with many other snakes.', 20, 5)

bob = Monster('Bob.', 'Bob.', 16, 4)

lizard = Monster('Elizabeth.', 'Think Mark Zuckerberg with, except he is a lizard. (wait...)', 30, 2)

startingRoom = Room('Starting Room', 'How did you even get here.', 0, 5)
	
registry["knife"] = Item('Knife', 'Cut of metal. Hardly a knife.', 5, 0, 3)

bagel = Item('Bagel', 'Round piece of bread. No cream cheese.', 3, 5, 0)

hammer = Item('Hammer', 'Very Fancy. Very Power. Very paper mache.', 4, 0, 4)

registry["nothing"] = Item('', '', 0, 0, 0)



damageTaken = 0
healthMods = 0
character = Item('You tell us.', 'No idea, ask whoevers next to you. If you are alone, then ha. Loser.', 9999, currentHealth, 0)
	
"""class Car():

wheels = 4

def __init__(self, make, model):
	self.make = make
	self.model = model

mustang = Car('Ford', 'Mustang')"""

"""possibleRooms = ['spookyCorridor', 'randRoom', 'idk', 'really idk', 'stop', 'now']
roomsLeft = len(possibleRooms)
""nextRoom = random.randint(1,25)""
nextRoom = random.randint(0, roomsLeft)
print (nextRoom)
""possibleRooms.append(Room)""
print (possibleRooms)"""


possibleMonsters = [auaojaj, bob, medusa, lizard]
charInventory.append('knife')
monstersInFight = []
gameWon = 0
possibleLoot = [bagel, hammer]
magicNumber = 0

while True:
	userTurn = input("What do you do? \n")
	dangerRating = dangerRating + 1
	print (dangerRating)
	monsterMatch = random.randint(1, 10)
	characterAttack = characterBaseAttack + weaponDamage
	currentHealth = 30 - damageTaken + healthMods
	

	

	if monsterMatch <= dangerRating and fightTrue == 0:
		monsterFound = possibleMonsters.pop(random.randint(0, 1))
		monstersInFight.append(monsterFound)
		fightTrue = 1
		print ("You found a monster! Lucky you, it is a ")
		print (monsterFound.name)
		monsterHealth = monsterFound.health
		print (monsterHealth)
		possibleDamage = monsterHealth + 1
	if (fightTrue == 1):
		dangerRating = 0
	if (userTurn == "MF"):
		if (currentRoomNumber <= 19):
			currentRoomNumber = currentRoomNumber + 5
			"""roomsLayout.remove(currentRoomNumber)
			roomsLayout.insert(currentRoomNumber, nextRoom)"""
		else:
			print ("You can not move in that direction")
	elif (userTurn == "MB"):
		if (currentRoomNumber >= 5):
			currentRoomNumber = currentRoomNumber - 5
		else:
			print ("You can not move in that direction")
	elif (userTurn == "ML"):
		if (currentRoomNumber != (0 or 5 or 10 or 15 or 20)):
			currentRoomNumber = currentRoomNumber - 1
		else:
			print ("You can not move in that direction")
	elif (userTurn == "MR"):
		if (currentRoomNumber != (4 or 9 or 14 or 19 or 24)):
			currentRoomNumber = currentRoomNumber + 1
		else:
			print ("You can not move in that direction")
	elif (userTurn == "Health"):
		print (currentHealth)
	elif (userTurn == "Inspect"):
		inspected = input("Inspect what? Enter the name \n")
		if inspected in registry and inspected != "nothing":
			theItem = registry[inspected]
		else:
			print ("Probably misspelled the item. Remember caps and correct spelling!")
			theItem = registry["nothing"]
		print (theItem.description)
	elif (userTurn == "PickUp"):
		print ()
		damageTaken = damageTaken + 9001 
		"""because its over 9000"""
	elif ((userTurn == "Retreat") and (fightTrue == 1)):
		print ("WOW. Coward. Anyways you run away, and take a slight bit of dmg")
		damageTaken = damageTaken + (random.randint(0, 5))
	elif ((userTurn == "Attack") and (fightTrue == 1)):
		for x in range(0, characterAttack):
			damageDone = random.randint(0, possibleDamage)
			if (damageDone >= monsterHealth):
				itemDropped = possibleLoot.pop(random.randint(0, len(possibleLoot)))
				fightTrue = 0
				monstersKilled = monstersKilled + 1
				possibleMonsters.append(monstersInFight.pop(0))
				print ("Nice. You killed the poor defenseless monster. I suggest you loot it's innocent corpse.")
				print ("Hey it dropped an item!")
				print (itemDropped)
			else:
				print ()
			if (monstersKilled == 3):
				print ("Congratulations! You've horribly killed lots of innocent monsters. You win (I guess).")
				gameWon = 1

		if (fightTrue == 1):
			print ("You failed to kill it. Ha. It swings back, because ya know, it's petty.")
			damageTaken = damageTaken + random.randint(0, monsterFound.damage)
		else:
			print()
	elif (userTurn == "LookAround"):
		print (currentRoomNumber)
		print ("You currently have this stuff (down)")
		print (charInventory)
		if (fightTrue == 1):
			print (monsterFound.description)
	elif (userTurn == "Commands"):
		print ("Commands, MoveForward, MoveBack, MoveLeft, MoveRight, Attack, Retreat, Inspect, LookAround, PickUp \n")
	else:
		print ("Maybe a typo? Or wrong command? Or stupidity? Either way please try again! And if you're trying to fight something, like a monster, then you obviously can't do that.")
	if (currentHealth <= 0):
		print ("gg you lost ur mom gey")
		userEndTurn = input("Do you want to try again? ")
		if (userEndTurn == "no u"):
			print ("Congratulations edgelord! You win!")
			break
		else:
			print ("IDK if you do or don't, just restart the program.")
			break
	if (gameWon == 1):
		break

