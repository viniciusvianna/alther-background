class Attribute:

    def __init__(self, name: str, total_value: int, current_value: int = -1, training_level: int = 0):
        self.name = name
        self.notation = name[0].upper()
        self.total_value = total_value
        self.training_level = training_level
        if current_value < 0:
            self.current_value = total_value
        else:
            self.current_value = current_value

    def __str__(self):
        return f"{self.name} {self.current_value}/{self.total_value}"

    def spend(self):
        if self.current_value > 0:
            self.current_value -= 1

    def recover(self):
        if self.current_value < self.total_value:
            self.current_value += 1

    def reset(self):
        self.current_value = self.total_value

