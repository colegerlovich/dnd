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
        print(jim.hp, "Is your health")
        print(Enemy.hp, "Is the enemies health")
        while jim.hp > 0 and Enemy.hp > 0:
            print("Combat starts")
            input("Press enter to fight:")
            dmg = random.randint(2,5)
            roll = random.randint(1,20)

            # if player roll plus modifiers is greater than the enemy ac than this happens.
            if (roll + jim.strength_mod) > Enemy.ac:
                Enemy.hp -= dmg
                print(Enemy.hp)
                print(f"You rolled a {roll} plus your strength mod of {jim.strength_mod}, so your roll is {roll + jim.strength_mod}")
                print("You hit was higher than your enemies armor class, roll for dmg")
                input("Press enter to roll for dmg:")
                print(f"You roll is for {jim.dmg} dmg")

            elif (roll + Enemy.strength_mod) <= Enemy.ac:
                enemy_roll = random.randint(1,20)
                print(f"You rolled {roll} plus your strength mod of {jim.strength_mod}, so your roll is {roll + jim.strength_mod}")
                print("This is less than the enemies armor class, now the", Enemy.name, "will roll to attack you")
                if (enemy_roll + Enemy.strengh_mod) > jim.ac:
                    print(f"The enemy swing at our hero {jim.name}")
                    print(f"The enemy deal {Enemy.dmg} to {jim.name}.")
                    jim_hp -= Enemy.dmg
                    print(jim_hp)

                elif(enemy_roll +Enemy.strengh_mod) <= jim_ac:
                    print("The attack dinks off the heros armor")

            else:
                print("Too low")
                print(dmg)


    def __str__(self):
        return "NAME: " + str(self.name) + " HP: " + str(self.hp) + " AC: " + str(self.ac) + " STRENGTH: " + str(self.strength) + " DEXTERITY: " + str(self.dexterity) + " CONSTITUTION" + str(self.constitution)

jim = Player("Jim", 20, 14, random.randint(2,5), 16, 15, 14, 16, 10, 6)
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

goblin = Enemy("Goblin", 7, 12, random.randint(1,4), 14, 12, 10, 15, 9, 11)
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

    for i in character_list:
        if character.lower() == "jim":
            print("You choose Jim")
            break
        else:
            print("pick one of the characters")
            character = input("> ")
            continue

#This is the left room after the start room. you can either right a goblin or sneak past him. If you fail sneaking then combat starts.
def sleeping_goblin():
    global jim_hp
    global character
    print("You see a goblin sleeping")
    print("Will you sneak past the goblin or try to fight him?")

    choice = input("> ")
    goblin_choice = ["fight", "sneak"]
    for i in goblin_choice:
        break
    else:
        print("You can choose to fight or sneak past the goblin")
        choice = input("> ")

    if choice.lower() == "fight":
        jim.combat(goblin)


#Creating a class for all of the other rooms
# class Room(object):
#     pass
#Starts the game by calling the start_room function
start_room()

# This starts the game, the user decides which path they would like to take.
print("You can take the path to the left or the right")

path = input("> ")
path = path.lower()
#calls the function sleeping_goblin if right is selected
if path == "left":
    sleeping_goblin()
elif path == "right":
    narrow_hallway()
#I need this to make the user input path again.
else:
    print("You can either go left or right")
    path = input("> ")

jim = Player("Jim", 20, 14, random.randint(2,5), 16, 15, 14, 16, 10, 6)
#print(jim)
goblin = Enemy("Goblin", 7, 12, random.randint(1,4), 14, 12, 10, 15, 9, 11)
#print(goblin)
