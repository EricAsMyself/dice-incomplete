from csv import DictReader
import random

class Die:
    #creatsed an instance of a Die
    def __init__(self):
        self.points = 0
        self.value = 0

    def roll(self):
        #Rolls the die and gets value. It also calculates the score.
        self.value = random.randint(1,6)
        if self.value == 1:
            self.points += 100
        elif self.value == 5:
            self.points += 50
