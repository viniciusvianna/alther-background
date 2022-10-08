from model.basic.definition.equipment import Equipment


class Armor(Equipment):

    def __init__(self, id_equipment, name, category=None, description=None, effect=None,
                 bonus=None):
        super().__init__(id_equipment, name, category, description, effect)

        if bonus is None:
            bonus = {}
        self._bonus = bonus

    def __str__(self):
        return f"{self._name} ({self._category})"
