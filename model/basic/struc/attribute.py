NEGATIVE_ATTRIBUTE = "O valor de um atributo não pode ser negativo"


class Attribute:

    def __init__(self, name: str,
                 total_value: int = 0,
                 current_value: int = -1,
                 temp_value: int = 0,
                 training_level: int = 0):
        self._name = name
        self._total_value = total_value
        self._temp_value = temp_value
        self._training_level = training_level
        if current_value < 0:
            self._current_value = total_value
        else:
            self._current_value = current_value

        self._notation = name[0].upper()

    def __str__(self):
        return f"{self._name} {self._current_value}/{self._total_value}"

    def __eq__(self, other):
        return self._name == other.name

    def __gt__(self, other):
        return self._total_value > other.total_value

    @property
    def name(self):
        return self._name

    @property
    def total_value(self):
        return self._total_value

    @property
    def current_value(self):
        return self._current_value

    @property
    def temp_value(self):
        return self._temp_value

    @property
    def training_level(self):
        return self._training_level

    @property
    def notation(self):
        return self._notation

    @total_value.setter
    def total_value(self, new_value):
        if new_value >= 0:
            self._total_value = new_value
        else:
            raise ValueError(NEGATIVE_ATTRIBUTE)

    @current_value.setter
    def current_value(self, new_value):
        if 0 <= new_value <= self._total_value:
            self._current_value = new_value
        elif new_value < 0:
            raise ValueError(NEGATIVE_ATTRIBUTE)
        else:
            raise ValueError("O valor atual do atributo não pode ser maior que seu valor total")

    @temp_value.setter
    def temp_value(self, new_value):
        if new_value >= 0:
            self._temp_value = new_value
        else:
            raise ValueError(NEGATIVE_ATTRIBUTE)

    @training_level.setter
    def training_level(self, new_level):
        if 0 <= new_level <= 5:
            self._training_level = new_level
        else:
            raise ValueError("O nível de treinamento só pode variar entre 0 e 5")

    def spend(self):
        if self._temp_value > 0:
            self._temp_value -= 1
            return True

        if self._current_value > 0:
            self._current_value -= 1
            return True

        return False

    def recover(self):
        if self._current_value < self._total_value:
            self._current_value += 1
            return True

        return False

    def reset(self):
        self._current_value = self._total_value

    def train(self):
        if self._training_level < 5:
            self._training_level += 1
            return True

        return False

    def detrain(self):
        if self._training_level > 0:
            self._training_level -= 1
            return True

        return False

