class Bonus:

    def __init__(self, place, dice):
        self.dice = dice
        self.place = place

    def __str__(self):
        return self.dice + self.place

