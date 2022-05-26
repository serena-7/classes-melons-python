"""This file should have our melon-type classes in it."""
from data import melons
from datetime import datetime

season_dict = {
    'Winter': [1, 2, 3],
    'Spring': [4, 5, 6],
    'Summer': [7, 8, 9],
    'Fall': [10, 11, 12]
}


class MelonOrder():
    def __init__(self, species, color, imported, difficult, shape, seasons, discount):
        self.species = species
        self.color = color
        self.imported = imported
        self.difficult = difficult
        self.shape = shape
        self.seasons = seasons
        self.discount = discount

    def get_price(self, qty):
        base_price = 5
        if self.difficult:
            base_price += 1
        price = base_price * qty
        if self.imported:
            price *= 1.5
        if self.shape != 'natural':
            price *= 2
        if self.discount != None:
            if qty >= self.discount['amount']:
                price *= self.discount['percent']
        return price

    def isAvailable(self):
        months = []
        for season in self.seasons:
            months += season_dict[season]

        current_month = datetime.now().month
        if current_month in months:
            return True
        else:
            return False


for melon in melons:
    globals()[melon[0].lower()] = MelonOrder(melon[0], melon[1], melon[2],
                                             melon[3], melon[4], melon[5], melon[6])

print(ogen.isAvailable())
