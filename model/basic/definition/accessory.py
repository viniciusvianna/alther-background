from model.basic.definition.equipment import Equipment


class Accessory(Equipment):

    def __init__(self, id_equipment, name, slot, category=None, description=None, effect=None):
        super().__init__(id_equipment, name, category, description, effect)

        self._slot = slot

    @property
    def slot(self):
        return self._slot
