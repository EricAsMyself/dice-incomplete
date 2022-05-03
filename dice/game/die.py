from csv import DictReader
import random
# from typing_extensions import Self


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
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



    # def roll(self, sides, amount):
    #     for i in range(0,amount):
    #         print(random.randint(1,sides))


    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
# dice = Die(12, 13)
# dice.roll(12, 13)

        # """Constructs a new instance of Die with a value and points attribute.

        # Args:
        #     self (Die): An instance of Die.
        # """

# 3) Create the roll(self) method. Use the following method comment.
        # """Generates a new random value and calculates the points.
        
        # Args:
        #     self (Die): An instance of Die.
        # """