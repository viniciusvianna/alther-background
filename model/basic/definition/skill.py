class Skill:

    def __init__(self, id_skill: str, id_path: str, name_skill: str, category: str, description: str, cost: int = 0):
        self._id_skill = id_skill
        self._id_path = id_path
        self._name_skill = name_skill
        self._category = category
        self._description = description
        self._cost = cost

    @property
    def id_skill(self):
        return self._id_skill

    @property
    def id_path(self):
        return self._id_path

    @property
    def name(self):
        return self._name_skill

    @property
    def category(self):
        return self._category

    @property
    def description(self):
        return self._description

    @property
    def cost(self):
        return self._cost

    def __str__(self):
        return f"{self._name_skill} ({self._category}): {self.description}"

    def __eq__(self, other):
        return self._id_skill == other.id_skill
