import  random

character_list = ['Jim']
# class Character(object):
#     def __init__(self, name, strength):
#         self.name = name
#         self.strength = strength
#         input("> ")
class Character():
    def __init__(self, name):
        self.name = name(input(">"))
        if i in character_list:
            if name == "Jim":
                print("You have choosen Jim. He is a mighty warrior")
            else:
                print("Pick a correct character")
    # def show(self):
    #     print(f"My name is {self.name}, and I am {self.strength} strong")

class Jim(Character):
    def speak(self):
        print("I am Jim")

class Samson(Character):
    def speak(self):
        print("I am samson")

class Rogthar(Character):
    def speak(self):
        print("I am Rogthar")

# c = Character("Bob", 19)
# c.show()
#
# j = Jim("Jim", 16)
# j.show()
#
# s = Samson("Samson", 10)
# s.show()
#
# r = Rogthar("Rogthar", 13)
# r.show()

Character("Jim")
