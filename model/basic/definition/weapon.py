from model.basic.definition.equipment import Equipment
from model.basic.struc.damage import Damage


class Weapon(Equipment):

    def __init__(self, id_equipment, name, category, description="", effect="",
                 damage: Damage = None,
                 bonus=None):

        super().__init__(id_equipment, name, category, description, effect)

        if damage is None:
            damage = Damage()
        self._damage = damage

        if bonus is None:
            bonus = []
        self._bonus = bonus

    def __str__(self):
        return f"{self._name}({self._category}) Dano: {self._damage}"

    @property
    def damage(self):
        return self._damage

    def roll_damage(self):
        return self._damage.roll_damage()

    def equip(self, char_attr):
        self._damage.equip(char_attr)

