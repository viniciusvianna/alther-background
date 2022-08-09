from bonus import Bonus
from damage import Damage
from dice import Dice


class Weapon:

    def __init__(self,
                 name: str,
                 category: str,
                 damage: Damage = Damage(),
                 description: str = "",
                 effect: str = "",
                 bonus: Bonus = Bonus()):

        self.name = name
        self.category = category
        self.damage = damage
        self.description = description
        self.effect = effect
        self.bonus = bonus
