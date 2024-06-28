import random


def modifier(score):
    return (score - 10) // 2


class Character:
    def __init__(self):
        self.strength = 18
        self.dexterity = 17
        self.constitution = 16
        self.intelligence = 15
        self.wisdom = 14
        self.charisma = 5
        self.hitpoints = 10 + self.constitution

    def ability(self):
        dices = sorted(random.randint(1, 6) for _ in range(4))
        return sum(dices[1:])
