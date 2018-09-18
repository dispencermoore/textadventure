import random
print ("\n Welcome to Spencer's Super Awesome Amazing Wonderful Text Adventure! \n");
print ("It is very simple. For every turn, you will input a command. In case you don't want to memorize the commands, just type 'Commands' whenever you want to know them all! For those of you with handy dandy memory, here is the *mostly full list. Move Forward (MF), Move Back (MB), Move Left (ML), Move Right (MR), Attack, Retreat, Inspect, LookAround (Which also tells you what you're carrying), PickUp. And that's all! Goodluck!");

roomsLayout = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
charInventory = []
roomLoot = []

startingRoomNumber = random.randint(0,24)
roomsLayout.remove(startingRoomNumber)
roomsLayout.insert(startingRoomNumber, 'startingRoom')
currentRoomNumber = startingRoomNumber
"""print (startingRoomNumber)
print (roomsLayout)"""

dangerRating = 0
fightTrue = 0
damageTaken = 0
healthMods = 0
weaponDamage = 0
monstersKilled = 0
characterBaseAttack = 2
currentHealth = 30 - damageTaken + healthMods
	
class Item():
	def __init__(self, name, description, value, health, damage):
		self.name = name
		self.description = description
		self.value = value
		self.health = health
		self.damage = damage

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
	
"""spookyCorridor = Room('Spooky Corridor', 'It is a corridor. And it is spooky.', 6, 2)"""

"""Below are all the possible room descriptions"""

a = "It's a corridor. And it's spooky"
b = "Big room. Suspiciously big."
c = "Stereotypical room. Offensively stereotypical."
d = "Looks like a chapel room. Except by people who worship... not chickens."
e = "There's like slime everywhere. Even in the air."
f = "59893315216"
g = "Dark, isolated, depressing, small, claustrophobic. Has a kitten picture."
h = "Imagine AUAOJAJ's room."
I = "There's a beanbag in the corner. You know the one."
j = "Very colorful room. And I mean language wise..."

roomDescriptions = [a, b, c, d, e, f, g, h, I, j]

auaojaj = Monster('AUAOJAJ.', 'The monsters name says it all tbh.', 10, 3)

medusa = Monster('SSSSSSSamantha.', 'Snake lady with many other snakes.', 20, 5)

bob = Monster('Bob.', 'Bob.', 16, 4)

lizard = Monster('Elizabeth.', 'Think Mark Zuckerberg, except he is a lizard. (wait...)', 30, 2)

startingRoom = Room('Starting Room', 'How did you even get here.', 0, 5)
	
registry["knife"] = Item('knife', 'Cut of metal. Hardly a knife.', 5, 0, 3)

registry["bagel"] = Item('bagel', 'Round piece of bread. No cream cheese.', 3, 5, 0)

registry["hammer"] = Item('hammer', 'Very Fancy. Very Power. Very paper mache.', 4, 0, 4)

registry["amulet"] = Item('amulet', 'Feels cursed. Probably just having a bad hair day.', 8, 0, 5)

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
charInventory.append("knife")
monstersInFight = []
gameWon = 0
possibleLoot = [registry["bagel"], registry["hammer"], registry["amulet"], registry["knife"]]
magicNumber = 0

while True:
	userRawTurn = input("What do you do? \n")
	userTurn = userRawTurn.lower()
	dangerRating = dangerRating + 1
	"""print (dangerRating)"""
	monsterMatch = random.randint(1, 10)
	characterAttack = characterBaseAttack + weaponDamage
	currentHealth = 30 - damageTaken + healthMods
	currentWeapon = charInventory.pop(0)
	charInventory.append(currentWeapon)
	weaponDamage = registry[currentWeapon].damage
	characterAttack = characterBaseAttack + weaponDamage
	"""print (currentRoomNumber)"""
	theRooms = len(roomDescriptions)
	
	if monsterMatch <= dangerRating and fightTrue == 0:
		monsterFound = possibleMonsters.pop(random.randint(0, 1))
		monstersInFight.append(monsterFound)
		fightTrue = 1
		print ("You found a monster! Lucky you, it is a ")
		print (monsterFound.name)
		monsterHealth = monsterFound.health
		"""print (monsterHealth)"""
		possibleDamage = monsterHealth + 1
	if (fightTrue == 1):
		dangerRating = 0
	if (userTurn == "mf" or userTurn == "moveforward"):
		if (currentRoomNumber <= 19):
			currentRoomNumber = currentRoomNumber + 5
			roomFound = (roomDescriptions.pop(random.randint(0, theRooms)))
			roomDescriptions.append(roomFound)
			print (roomFound)
		else:
			print ("You can not move in that direction")
	elif (userTurn == "mb" or userTurn == "moveback" or userTurn == "movebackward"):
		if (currentRoomNumber >= 5):
			currentRoomNumber = currentRoomNumber - 5
			roomFound = (roomDescriptions.pop(random.randint(0, theRooms)))

			roomDescriptions.append(roomFound)
			print (roomFound)
		else:
			print ("You can not move in that direction")
	elif (userTurn == "ml" or userTurn == "moveleft"):
		if (currentRoomNumber != (0 or 5 or 10 or 15 or 20)):
			currentRoomNumber = currentRoomNumber - 1
			roomFound = (roomDescriptions.pop(random.randint(0, theRooms)))
			roomDescriptions.append(roomFound)
			print (roomFound)
		else:
			print ("You can not move in that direction")
	elif (userTurn == "mr" or userTurn == "moveright"):
		if (currentRoomNumber != (4 or 9 or 14 or 19 or 24)):
			currentRoomNumber = currentRoomNumber + 1
			roomFound = (roomDescriptions.pop(random.randint(0, theRooms)))
			roomDescriptions.append(roomFound)
			print (roomFound)
		else:
			print ("You can not move in that direction")
	elif (userTurn == "health" or userTurn == "hp"):
		print (currentHealth)
	elif (userTurn == "inspect"):
		inspected = input("Inspect what? Enter the name \n")
		if inspected in registry and inspected != "nothing":
			theItem = registry[inspected]
		else:
			print ("Probably misspelled the item. Remember caps and correct spelling!")
			theItem = registry["nothing"]
			print (theItem.description)
	elif (userTurn == "pickup" or userTurn == "pu"):
		pickedUp = input("Unless you are grabbing air (which you can if you want), please specify what you are grabbing \n")
		if (pickedUp in roomLoot and pickedUp != "bagel"):
			charInventory = []
			charInventory.append(pickedUp)
		elif (pickedUp == "air"):
			print ("I mean, I did say you could... smart ass.")
		elif (pickedUp == "bagel"):
			damageTaken = damageTaken - 3
			print ("So, you like pick up and eat the bagel. It heals you. It was not tasty.")
		else:
			print ("That Item is not in your current room. Basically you do not have 20 meter arms.")
	elif ((userTurn == "retreat") and (fightTrue == 1)):
		print ("WOW. Coward. Anyways you run away, and take a slight bit of dmg")
		damageTaken = damageTaken + (random.randint(0, 5))
		fightTrue == 0
		monstersInFight = []
	elif ((userTurn == "attack") and (fightTrue == 1)):
		for x in range(0, characterAttack):
			damageDone = random.randint(0, possibleDamage)
			if (damageDone >= monsterHealth and fightTrue == 1):
				trueLoot = len(possibleLoot) - 1
				itemDropped = (possibleLoot.pop(random.randint(0, trueLoot))).name
				roomLoot.append(registry[itemDropped].name)
				fightTrue = 0
				monstersKilled = monstersKilled + 1
				"""print (monstersInFight)"""
				possibleMonsters.append(monstersInFight.pop(0))
				print ("Nice. You killed the poor defenseless monster. I suggest you steal from it's innocent corpse.")
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
	elif (userTurn == "lookaround" or userTurn == "la"):
		print (currentRoomNumber)
		print ("You currently have this stuff (down)")
		print (charInventory)
		if (fightTrue == 1):
			print ("Here are some of those monster stats.")
			print ("Like the health, which is below")
			print (monsterHealth)
			print ("And the description, which is")
			print (monsterFound.description)
	elif (userTurn == "commands"):
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

