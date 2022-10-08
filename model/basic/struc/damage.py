from model.basic.struc.dice import Dice
from model.basic.struc.attribute import Attribute

notations = {"C": "Corpo", "M": "Mente", "F": "Foco", "E": "Espírito", "S": "Social", "N": "Natureza"}


class Damage:

    def __init__(self, dice: Dice = None, attr: Attribute = None, factor=0.0, bonus: int = 0):

        self.dice = dice
        if attr is None:
            attr = Attribute("Corpo")
        self.attr = attr
        self.factor = factor
        self.bonus = bonus

    def __str__(self):
        to_string = ""
        if self.dice is not None:
            to_string += f"{self.dice}"
        if self.attr is not None:
            if self.factor > 1.0:
                to_string += f"+{self.factor}{self.attr.notation}"
            elif 1.0 > self.factor > 0.0:
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

    @staticmethod
    def from_string(damage):
        d = damage.find('d')
        p = damage.find('+')

        number = int(damage[:d])
        sides = int(damage[d+1:p])

        if damage[p+1] in notations.keys():
            attr = Attribute(notations[damage[p+1]])
            factor = 1 / float(damage[p+2:])
        else:
            notation = damage[-1]
            attr = Attribute(notations[notation])
            factor = float(damage[p+1:damage.find(notation)])

        dice = Dice(number, sides)

        return Damage(dice, attr, factor)






