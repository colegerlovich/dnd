import random
import xlsxwriter

global player

workbook = xlsxwriter.Workbook('C:/Users/Cole Gerlovich/Desktop/dnd.xlsx')
worksheet = workbook.add_worksheet()
weapons = (
    ['sword', 6],
    ['mace', 8],
    ['dagger', 5],
)

row = 0
col = 0

for item, dmg in (weapons):
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, dmg)
    row += 1

workbook.close()


character_list = ["Rogthar", "Samson", "Jim"]
character_inventory = []

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
        self.wisdom_mod = (self.wisdom - 10) // 2
        self.charisma_mod = (self.charisma - 10) // 2

    def die(self):
        if self.hp <= 0:
            print("While", self.name, "did not make it through the dungeon, he sure did have a good time.")

    def combat(self, Enemy):
        print(f"Prepare to fight {Enemy.name}")
        print(self.hp, "Is your health")
        print(Enemy.hp, "Is the enemies health")
        while self.hp > 0 and Enemy.hp > 0:
            print("Combat starts")
            input("Press enter to fight:")
            dmg = random.randint(2,5)
            roll = random.randint(1,20)

            # if player roll plus modifiers is greater than the enemy ac than this happens.
            if (roll + self.strength_mod) > Enemy.ac:
                Enemy.hp -= dmg
                print(Enemy.hp)
                print(f"You rolled a {roll} plus your strength mod of {self.strength_mod}, so your roll is {roll + self.strength_mod}.")
                print("You hit was higher than your enemies armor class, roll for dmg.")
                input("Press enter to roll for dmg:")
                print(f"You roll is for {self.dmg} dmg.")

            elif (roll + Enemy.strength_mod) <= Enemy.ac:
                enemy_roll = random.randint(1,20)
                print(f"You rolled {roll} plus your strength mod of {self.strength_mod}, so your roll is {roll + self.strength_mod}.")
                print("This is less than the enemies armor class, now the", Enemy.name, "will roll to attack you.")
                if (enemy_roll + Enemy.strength_mod) > self.ac:
                    print(f"The enemy swing at our hero {self.name}.")
                    print(f"The enemy deal {Enemy.dmg} to {self.name}.")
                    self.hp -= Enemy.dmg
                    print(self.hp)

                elif(enemy_roll +Enemy.strength_mod) <= self.ac:
                    print("The attack dinks off the heros armor.")

            if Enemy.hp <=0:
                Enemy.die()
            elif self.hp <=0:
                self.die()

            else:
                print("Too low")
                print(dmg)

    def stealth(self, Enemy):
        self.stealth = random.randint(1,20) + self.constitution_mod
        print("You rolled", self.stealth,".")

        if self.stealth >= Enemy.enemy_rolls():
            print("The enemy rolled",Enemy.enemy_rolls(),".")
            print("You sneak past the", Enemy.name,".")

        elif self.stealth < Enemy.enemy_rolls():
            print("wow, you failed... *sigh*")
            input("Press enter to begin combat: ")
            self.combat(Enemy)



    def __str__(self):
        return "NAME: " + str(self.name) + " HP: " + str(self.hp) + " AC: " + str(self.ac) + " STRENGTH: " + str(self.strength) + " DEXTERITY: " + str(self.dexterity) + " CONSTITUTION" + str(self.constitution)

jim = Player("Jim", 20, 14, random.randint(2,5), 16, 15, 14, 16, 10, 6)
rogthar= Player("Rogthar", 26, 12, random.randint(3,6), 18, 12, 13, 11, 9, 12)
global jim_hp
# creating the enemy class. The enemy needs the standard stats that our player will need. I am choosing to not inherate from the player class.
class Enemy(object):

    def __init__(self, name, hp, ac, dmg, strength, dexterity, constitution,\
    intelligence, wisdom, charisma):
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

    def die(self):
        print(self.name, "has passed")

    def enemy_rolls(self):
        self.con_roll = random.randint(1,20) + self.constitution_mod
        return self.con_roll

goblin = Enemy("Goblin", 7, 12, random.randint(1,7), 14, 12, 10, 15, 9, 11)
# This is the start of the game. This function needs to be called first
# You decide the character you would like to play as this game.
# Currently we have only made Jim. Will need to update later
def start_room():
    global character
    print("""
    Hello adventurer, I hope you are ready for this journey.
    You will be able to play as a few characters.
    You can be Rogthar the destoryer, Samson the slayer or Jim.
    """)
    #Input from user deciding on which character to play as
    character = input("> ")
    print(character)

    while character not in character_list:
        if character.lower() == "jim":
            print("You choose Jim")
            break
        else:
            print("pick one of the characters")
            character = input("> ")
            continue

# This is the left room after the start room. You can sneak or fight.
# If you fight then the combat method is called from the Player class.
# If you sneak then the sneak method is called from the Player class.
# If you fail sneaking then you will call combat method from the Player class.
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

# Jim is still the place holder for this. I need to have the player input replace this.
    if choice.lower() == "fight":
        jim.combat(goblin)

# Jim is still the place holder for this. I need to have the player input replace this.
    elif choice.lower() == "sneak":
        jim.stealth(goblin)

    choice_2 = input("Do you loot the goblin or continue to the next room?")
    choice_2 = choice_2.lower()
    print(choice_2)

    while choice_2 != "loot" or "next room":
        choice_2 = input("You can loot or go to the 'next room'")

        if choice_2 == "loot":
            character_inventory.append("wax_statue")
            print("The goblin had a wax figure in his pocket.")
            print("The figure appears to be some sort of god for the goblins.")
            print("With nothing else to do you go to the next room.")
            break

        elif choice_2 == "next room":
            break

    stats_teacher()

def stats_teacher():
    print("welcome to class")

    # if choice_2 == "loot":
    #     print("The goblin had a wax figure in his pocket.")
    #     print("The figure appears to be some sort of god for the goblins.")
    #
    # else choice_2 == "next room":
    #     print("You go to the next room")

# This is the right room after the start room. You have to get past the wavy man.
# The wavy_man has a dictionary of what he is good at, if you list something
# that isn't in the wavy_man dictionary then you defeat him.
def wavy_man():

    print("\nYou enter a narrow hallway with a torch lighting your way.\nAll of the sudden you see a figure in the hallway")
    print("\nYou see that the man is waving his arms around in a frenzy. They say 'How are you supposed to be wavier than the wavy man?'")
    print("\nYou bring out your sword and attempt to slash the wavy man, but he is just too wavy")
    print("\nThey keep repeating 'How are you supposed to be wavier than the wavy man?' 'How are you supposed to be wavier than the wavy man?' 'How are you supposed to be wavier than the wavy man?'")
    wavy_man_dict = {"cars": "I've got a better car",
                "songs": "Ive got beter songs",
                "looks": "I look better",
                "life": "I just live better than you",
                "best": "I'm the best"}
    best = input("\nMaybe you can best the wavy man in something other than being wavy.\nWe all know the most important things in life right?\nThat's right! Cars, songs, looks and life are the most important things.\nPut what you can beat the wavy man at: ")
    best = best.lower()


    while best not in wavy_man_dict:
        print("moo")

        if wavy_man_dict:
            print(f"{best} was not in dictionary")
            best = input("Select something else are better than the wavy_man at: ")
        else:
            print(wavy_man_dict)
            input("Press enter to exit")
            break

    # while best in wavy_man:
    #     print(wavy_man[best])
    #     print("The wavy man slaps ", self.name, "dealing 2 damage")
    #     self.hp -= 2
    #     print(self.hp)
    #     best = input("What are you better at than the wavy_man? >: ")

#Creating a class for all of the other rooms
# class Room(object):
#     pass
#Starts the game by calling the start_room function

start_room()

# This starts the game, the user decides which path they would like to take.
print("You can take the path to the left or the right")

path = input("> ")
path = path.lower()
# calls the function sleeping_goblin if left is selected
while path != "left" and "right":
# while path != left and path != right
    print("You can either go left or right")
    path = input("> ")

if path == "left":
    sleeping_goblin()
# calls the function wavy_man if right is selected
elif path == "right":
    wavy_man()


#jim = Player("Jim", 20, 14, random.randint(2,5), 16, 15, 14, 16, 10, 6)
#print(jim)
#goblin = Enemy("Goblin", 7, 12, random.randint(1,4), 14, 12, 10, 15, 9, 11)
#print(goblin)
