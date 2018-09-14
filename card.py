# Card class from deck of cards exercise. Using for unit testing section
# Tests: __init__ and __repr__ functions

from random import shuffle

class Card:

    available_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    available_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if suit not in Card.available_suits:
            raise ValueError  # (f"{suit} is not a valid suit.")
        elif str(value) not in Card.available_values:
            raise ValueError  # (f"{value} is not a valid value.")
        else:
            self.suit = suit
            self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)  # f"{self.value} of {self.suit}"