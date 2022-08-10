import random

global character

character_list = ["Rogthar", "Samson", "Jim"]

#creating the starting room
def start_room():
    global character
    print("""
    Hello adventurer, I hope you are ready for this journey.
    You will be able to play as a few characters.
    You can be Rogthar the destoryer, Samson the slayer or Jim
    """)
    #Input from user deciding on which character to play as
    character = input("> ")

    for i in character_list:
        if character == "jim" or character == "Jim":
            break
            print("You choose Jim")
        else:
            print("pick one of the characters")
            character = input("> ")
#Starts the game by calling the start_room function
start_room()
