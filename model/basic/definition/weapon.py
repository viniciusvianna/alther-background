from model.basic.struc.damage import Damage


class Weapon:

    def __init__(self,
                 name: str,
                 category: str,
                 damage: Damage = None,
                 description: str = "",
                 effect: str = "",
                 bonus=None):

        self.name = name
        self.category = category
        if damage is None:
            damage = Damage()
        self.damage = damage
        self.description = description
        self.effect = effect
        if bonus is None:
            bonus = []
        self.bonus = bonus

    def __str__(self):
        return f"{self.name}({self.category}) Dano: {self.damage}"

