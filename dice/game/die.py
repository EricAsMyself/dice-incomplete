from csv import DictReader
import random

class Die:
    def __init__(self):
        self.points = 0
        self.value = 0

    def roll(self):
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points += 100
        elif self.value == 5:
            self.points += 50
