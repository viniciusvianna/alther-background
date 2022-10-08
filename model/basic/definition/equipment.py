class Equipment:

    def __init__(self,
                 id_equipment: str,
                 name: str,
                 category=None,
                 description=None,
                 effect=None):

        if category is None:
            category = ""

        if description is None:
            description = ""

        if effect is None:
            effect = ""

        self._id_equipment = id_equipment
        self._name = name
        self._category = category
        self._description = description
        self._effect = effect

