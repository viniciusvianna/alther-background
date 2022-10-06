from model.basic.struc.bonus import Bonus
from model.basic.struc.dice import Dice


# Action é um conjunto de dados que representam a capacidade do personagem de executar aquela ação
# O construtor da classe aceita parâmetro vazio para o dicionário de dados, pois inicializa a mesma com o
# número de dados padrão para o nível 1 de personagem (1d8)


class Action:

    def __init__(self, name: str, all_dice=None):
        if all_dice is None:
            all_dice = {'d4': Dice(0, 4),
                        'd6': Dice(0, 6),
                        'd8': Dice(1, 8),
                        'd10': Dice(0, 10),
                        'd12': Dice(0, 12),
                        'd20': Dice(0, 20)}
        self.name = name
        self.all_dice = all_dice

    def __str__(self):
        return f"{self.name} {self.show_all_dice()}"

    def roll_action(self):
        result = 0
        for dice in self.all_dice.values():
            result += dice.roll()  # O resultado da rolagem deve ser a soma da rolagem de todos os dados da ação

        return result

    def show_all_dice(self):
        show = ""
        for dice in self.all_dice.values():
            show += f"{dice} "

        return show

    # Tanto a função de remoção como adição de dados recebem um dado como parâmetro para facilitar a legibilidade
    def add_dice(self, dice: Dice):
        self.all_dice[f'd{dice.sides}'].quantity += dice.quantity

    def remove_dice(self, dice: Dice):
        self.all_dice[f'd{dice.sides}'].quantity -= dice.quantity

    def apply_bonus(self, bonus: Bonus):
        if bonus.action == self.name:
            self.all_dice[bonus.dice.category()] += bonus.dice
            return True
        return False
