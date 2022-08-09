from bonus import Bonus
from dice import Dice


class Damage:

    def __init__(self, dice: Dice = None, attr: str = None, factor=0, bonus: Bonus = None):

        self.dice = dice
        self.attr = attr
        self.factor = factor
        self.bonus = bonus

    def __str__(self):
        to_string = ""
        if self.dice is not None:
            to_string += f"{self.dice}"
        if self.attr is not None:
            if self.factor > 1:
                to_string += f"+ {self.factor}{self.attr[0]}"
            elif 1 > self.factor > 0:
                to_string += f"+ {self.attr[0]}{1//self.factor}"
            else:
                to_string += f"+ {self.attr[0]}"
        if self.bonus is not None:
            to_string += f"+ {self.bonus}"

        return to_string


