import random


class Dice:
    def roll(self):
        x1 = random.randint(1, 6)
        x2 = random.randint(1, 6)
        return x1, x2


dice = Dice()
print(dice.roll())
