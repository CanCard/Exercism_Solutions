import math, random

def random_dice():
    numbers = []
    sum = 0
    for i in range(4):
        roll = random.randint(1,6)
        numbers.append(roll)
    numbers.sort()
    x,y,z,_ = numbers[::-1]
    sum = x + y + z
    return sum
    
class Character:
    def __init__(self):
        self.strength = random_dice()
        self.dexterity = random_dice()
        self.constitution = random_dice()
        self.intelligence = random_dice()
        self.wisdom = random_dice()
        self.charisma = random_dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return random_dice()
        
        
def modifier(value):
    value = math.floor((value - 10) / 2)
    return value
