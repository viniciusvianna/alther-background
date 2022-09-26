from model.basic.struc.dice import Dice
from model.basic.struc.attribute import Attribute


class Damage:

    def __init__(self, dice: Dice = None, attr: Attribute = None, factor=0, bonus: int = 0):

        self.dice = dice
        if attr is None:
            attr = Attribute("body")
        self.attr = attr
        self.factor = factor
        self.bonus = bonus

    def __str__(self):
        to_string = ""
        if self.dice is not None:
            to_string += f"{self.dice}"
        if self.attr is not None:
            if self.factor > 1:
                to_string += f"+{self.factor}{self.attr.notation}"
            elif 1 > self.factor > 0:
                to_string += f"+{self.attr.notation}{int(1//self.factor)}"
            else:
                to_string += f"+{self.attr.notation}"
        if self.bonus > 0:
            to_string += f"+{self.bonus}"
        elif self.bonus < 0:
            to_string += f"-{self.bonus}"

        return to_string

    def roll_damage(self):
        result = 0
        if self.dice is not None:
            result += self.dice.roll()
        if self.attr is not None:
            result += int(self.attr.total_value * self.factor)
        if self.bonus is not None:
            result += self.bonus

        return result

    def equip(self, char_attr: Attribute):
        self.attr = char_attr


