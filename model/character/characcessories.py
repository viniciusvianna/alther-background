from model.basic.definition.accessory import Accessory


class CharAccessories:

    def __init__(self,
                 hands: Accessory = None,
                 body: Accessory = None,
                 head: Accessory = None,
                 feet: Accessory = None
                 ):
        if hands is None:
            hands = ""
        if body is None:
            body = ""
        if head is None:
            head = ""
        if feet is None:
            feet = ""

        self._accessories = {'hands': hands, 'body': body, 'head': head, 'feet': feet}

    def __str__(self):
        result = f"Accessories:\n "
        for accessory in self._accessories:
            result += f"{accessory}\n"
        return result

    @property
    def hands(self):
        return self._accessories['hands']

    @property
    def body(self):
        return self._accessories['body']

    @property
    def head(self):
        return self._accessories['head']

    @property
    def feet(self):
        return self._accessories['feet']

    def equip(self, accessory):
        if accessory.slot in self._accessories.keys():
            self._accessories[accessory.slot] = accessory

    def unequip(self, slot):
        self._accessories[slot] = ""

