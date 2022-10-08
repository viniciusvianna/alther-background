from model.basic.definition.armor import Armor
from model.basic.definition.equipment import Equipment
from model.basic.definition.weapon import Weapon

WRONG_SLOT = "This equipment cannot be in this slot"


class CharEquipments:

    def __init__(self,
                 hand1: Equipment = None,
                 hand2: Equipment = None,
                 body: Equipment = None
                 ):

        if hand1 is None:
            hand1 = ""
        if hand2 is None:
            hand2 = ""
        if body is None:
            body = ""

        self._equipments = {'hand1': hand1, 'hand2': hand2, 'body': body}

    def __str__(self):
        result = f"Equipments:\n"
        for equipment in self._equipments.items():
            result += f"{equipment[0]}: {equipment[1]}\n"
        return result

    @property
    def hand1(self):
        return self._equipments['hand1']

    @hand1.setter
    def hand1(self, value):
        if isinstance(value, Weapon):
            self._equipments['hand1'] = value
        else:
            raise ValueError(WRONG_SLOT)

    @property
    def hand2(self):
        return self._equipments['hand2']

    @hand2.setter
    def hand2(self, value):
        if isinstance(value, Weapon):
            self._equipments['hand2'] = value
        else:
            raise ValueError(WRONG_SLOT)

    @property
    def body(self):
        return self._equipments['body']

    @body.setter
    def body(self, value):
        if isinstance(value, Armor):
            self._equipments['body'] = value
        else:
            raise ValueError(WRONG_SLOT)

    def equip(self, new_equipment, slot):
        if isinstance(new_equipment, Weapon):
            if slot == 'hand1' or slot == 'hand2':
                self._equipments[slot] = new_equipment
            else:
                raise ValueError(WRONG_SLOT)
        elif isinstance(new_equipment, Armor):
            if slot == 'body':
                self._equipments['body'] = new_equipment
            else:
                raise ValueError(WRONG_SLOT)
        else:
            raise ValueError('Invalid equipment')

    def unequip(self, slot):
        self._equipments[slot] = ""

