class Equipment:

    def __init__(self,
                 id_equipment: str,
                 name: str,
                 category: str,
                 description: str = "",
                 effect: str = ""):

        self._id_equipment = id_equipment
        self._name = name
        self._category = category
        self._description = description
        self._effect = effect

