import random

global player

character_list = ["Rogthar", "Samson", "Jim"]

# creating the player class
class Player(object):

    def __init__(self, name, hp, ac, dmg, strength, dexterity, constitution, intelligence, wisdom,
    charisma):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2

    def combat(self, Enemy):
        print(f"Prepare to fight {Enemy.name}")

    def __str__(self):
        return "NAME: " + str(self.name) + " HP: " + str(self.hp) + " AC: " + str(self.ac) + " STRENGTH: " + str(self.strength) + " DEXTERITY: " + str(self.dexterity) + " CONSTITUTION" + str(self.constitution)

# creating the enemy class. The enemy needs the standard stats that our player will need. I am choosing to not inherate from the player class.
class Enemy(object):

    def __init__(self, name, hp, ac, dmg, strength, dexterity, constitution, intelligence, wisdom,
    charisma):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.dmg = dmg
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.strength_mod = (self.strength - 10) // 2
        self.dexterity_mod = (self.dexterity - 10) // 2
        self.constitution_mod = (self.constitution - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.intelligence_mod = (self.intelligence - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2

    def __str__(self):
        return "NAME: " + str(self.name) + " HP: " + str(self.hp) + " AC: " + str(self.ac) + " STRENGTH: " + str(self.strength) + " DEXTERITY: " + str(self.dexterity) + " CONSTITUTION" + str(self.constitution)

#creating the starting room
def start_room():
    global player
    print("""
    Hello adventurer, I hope you are ready for this journey.
    You will be able to play as a few characters.
    You can be Rogthar the destoryer, Samson the slayer or Jim
    """)
    #Input from user deciding on which character to play as
    character = input("> ")

    for character in character_list:
        if character == "jim" or character == "Jim":
            break
            print("You choose Jim")
        else:
            print("pick one of the characters")
            character = input("> ")

#Creating a class for all of the other rooms
# class Room(object):
#     pass
#Starts the game by calling the start_room function
jim = Player("Jim", 20, 14, random.randint(2,5), 16, 15, 14, 16, 10, 6)
print(jim)
goblin = Enemy("Goblin", 7, 12, random.randint(1,4), 14, 12, 10, 15, 9, 11)
print(goblin)
