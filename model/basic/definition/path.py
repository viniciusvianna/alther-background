pc_per_level_tier_1 = {2: 100, 3: 300, 4: 500, 5: 800, 6: 1100, 7: 1500, 8: 2000, 9: 2500, 10: 3000}
pc_per_level_tier_2 = {2: 1000, 3: 2000, 4: 3000, 5: 5000, 6: 6000, 7: 7000, 8: 8000, 9: 10000, 10: 12000}
pc_per_level_tier_3 = {2: 3000, 3: 6000, 4: 9000, 5: 12000, 6: 16000, 7: 20000, 8: 24000, 9: 30000, 10: 40000}


class Path:

    def __init__(self,
                 id_path: str,
                 name_path: str,
                 tier: int = 1,
                 level: int = 1,
                 total_pc: int = 0,
                 current_pc: int = 0,
                 master: bool = False):

        self._id_path = id_path
        self._name_path = name_path
        self._tier = tier
        self._level = level
        self._total_pc = total_pc
        self._current_pc = current_pc
        self._master = master

    @property
    def id_path(self):
        return self._id_path

    @property
    def name_path(self):
        return self._name_path

    @property
    def tier(self):
        return self._tier

    @property
    def level(self):
        return self._level

    @property
    def total_pc(self):
        return self._total_pc

    @total_pc.setter
    def total_pc(self, new_value):
        self._current_pc += new_value - self._total_pc
        self.total_pc = new_value
        self._level_up()
        self._become_master()

    @property
    def current_pc(self):
        return self._current_pc

    @property
    def is_master(self):
        return self._master

    def _level_up(self):
        if self._tier == 1:
            pc_per_level = pc_per_level_tier_1
        elif self._tier == 2:
            pc_per_level = pc_per_level_tier_2
        elif self._tier == 3:
            pc_per_level = pc_per_level_tier_3
        else:
            raise ValueError("Wrong tier")

        for level in pc_per_level.items():
            if self._total_pc >= level[1]:
                self._level = level[0]

    def _become_master(self):
        if self._level == 10:
            self._master = True

    def spend_pc(self, value):
        if self._current_pc >= value:
            self._current_pc -= value
        else:
            print("You can't afford this")

    def __str__(self):
        return f"{self._name_path}: lv.{self._level} {self._current_pc}/{self._total_pc} PC"

    def __eq__(self, other):
        return self._id_path == other.id_path
