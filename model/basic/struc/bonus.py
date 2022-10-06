from model.basic.struc.dice import Dice


class Bonus:

    def __init__(self, action: str, dice: Dice):
        self.dice = dice
        self.action = action

    def __str__(self):
        return self.dice + self.action

