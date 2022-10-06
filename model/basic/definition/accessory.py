from model.basic.definition.equipment import Equipment


class Accessory(Equipment):

    def __init__(self, id_equipment, name, category, slot, description="", effect=""):
        super().__init__(id_equipment, name, category, description, effect)

        self._slot = slot

    @property
    def slot(self):
        return self._slot
