from random import randrange as rdr

# Classe para representar melhor os dados no formato padrão de rpg (QdS)


class Dice:

    def __init__(self, quantity: int, sides: int):
        self.sides = sides
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity}d{self.sides}"  # Imprime o dado no formato padrão

    def roll(self):
        return self.quantity * rdr(1, self.sides + 1) # O dado deve ser capaz de se rolar
