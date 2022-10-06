from model.basic.definition.accessory import Accessory
from model.basic.definition.armor import Armor
from model.basic.definition.equipment import Equipment
from model.basic.definition.weapon import Weapon

WRONG_SLOT = "Você não pode equipar este esquipamento no slot pedido"


class CharEquipments:

    def __init__(self,
                 hand1: Equipment = None,
                 hand2: Equipment = None,
                 body: Equipment = None,
                 head: Equipment = None,
                 feet: Equipment = None,
                 extra: Equipment = None):
        if hand1 is None:
            hand1 = Equipment('000000', "", "")
        if hand2 is None:
            hand2 = Equipment('000000', "", "")
        if body is None:
            body = Equipment('000000', "", "")
        if head is None:
            head = Equipment('000000', "", "")
        if feet is None:
            feet = Equipment('000000', "", "")
        if extra is None:
            extra = Equipment('000000', "", "")

        self._hand1 = hand1
        self._hand2 = hand2
        self._body = body
        self._head = head
        self._feet = feet
        self._extra = extra

    def get_hand(self, hand):
        if hand == 'hand1':
            return self._hand1
        elif hand == 'hand2':
            return self._hand2
        else:
            raise ValueError("No hand")

    def equip(self, new_equipment, slot=None):
        if slot is None:
            if new_equipment.slot == "head":
                self._head = new_equipment
            elif new_equipment.slot == "feet":
                self._feet = new_equipment
            elif new_equipment.slot == "extra":
                self._extra = new_equipment
            else:
                raise ValueError(WRONG_SLOT)
        else:
            if isinstance(new_equipment, Weapon):
                if slot == "hand1":
                    self._hand1 = new_equipment
                elif slot == "hand2":
                    self._hand2 = new_equipment
                else:
                    raise ValueError(WRONG_SLOT)
            elif isinstance((new_equipment, Armor)):
                if slot == "body":
                    self._body = new_equipment
                elif slot == "hand1":
                    self._hand1 = new_equipment
                elif slot == "hand2":
                    self._hand2 = new_equipment
                else:
                    raise ValueError(WRONG_SLOT)
            else:
                raise ValueError("Falha no equipamento")

