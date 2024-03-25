import csv
from datetime import datetime as dt

class Guitar:
    def __init__(self, brand="", made_year=0, price=0):

        self.brand = brand
        self.made_year = made_year
        self.price = price

    def __str__(self):
        return f"{self.brand} ({self.made_year}) : ${self.price:,.2f}"

    def get_age(self):
        return dt.now().year - self.made_year

    def is_vintage(self):
        return self.get_age() >= 50

    def __lt__(self, other):
        return self.made_year < other.made_year
