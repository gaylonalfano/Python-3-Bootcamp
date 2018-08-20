'''
Introduction

Your goal in this exercise is to implement two classes, Card  and Deck .

Specifications

Card

Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)


Deck:
Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.


'''

from random import shuffle

class Card:

    available_suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    available_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, suit, value):
        if suit not in Card.available_suits:
            raise ValueError(f"{suit} is not a valid suit.")
        elif str(value) not in Card.available_values:
            raise ValueError(f"{value} is not a valid value.")
        else:
            self.suit = suit
            self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:


    def __init__(self):
        # Save each instance of Card to the cards list attribute -- how?
        # Not fully sure about the self.name = name, self.cards = cards naming/meaning?
        # Can set self.cards to a list instead of cards???
        # **Think of these attributes as key: value pairs. See Chicken Coop hard set eggs
        self.cards = [Card(s, v) for v in Card.available_values for s in Card.available_suits]


    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self)

    def _deal(self, number=1):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() < number:
            raise ValueError(f"Only {self.count()} card(s) left. Please try another amount.")
        else:
            return [self.cards.pop() for x in range(number)]

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, number):
        return self._deal(number)


c1 = Card('Diamonds', 4)
c2 = Card('Hearts', 5)

print(c1)
print(c2.value)

deck1 = Deck()
print(deck1)
print(deck1.count())
print(deck1.cards[0])
print(deck1._deal(1))
print(deck1.count())

