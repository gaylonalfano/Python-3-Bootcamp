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
            raise ValueError  # (f"{suit} is not a valid suit.")
        elif str(value) not in Card.available_values:
            raise ValueError  # (f"{value} is not a valid value.")
        else:
            self.suit = suit
            self.value = value

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)  # f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        # Save each instance of Card to the cards list attribute -- how?
        # Not fully sure about the self.name = name, self.cards = cards naming/meaning?
        # Can set self.cards to a list instead of cards???
        # **Think of these attributes as key: value pairs. See Chicken Coop hard set eggs
        self.cards = [Card(s, v) for v in Card.available_values for s in Card.available_suits]

    def __repr__(self):
        return f"Deck of {self.count()} cards"
        #  "Deck of {} cards".format(len(self.cards))
        #  f"Deck of {len(self.cards)} cards"

    def __iter__(self):
        return iter(self.cards)
    '''
    Once we learn GENERATORS, we can also write it like this:
    def __iter__(self):
        for card in self.cards:
            yield card
    '''
    def reset(self):
        '''Reset the deck back to original init state'''
        self.cards = [Card(s, v) for v in Card.available_values for s in Card.available_suits]
        return self

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        return shuffle(self.cards)  # !!! Forgot to return self.CARDS!!

    def _deal(self, number=1):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        elif self.count() < number:  # Use try/except here?
            print("Only {} cards left. Will deal all remaining cards.".format(self.count()))
            dealt = [self.cards.pop() for x in range(self.count())]
            return dealt[-number:]
        else:
            dealt = [self.cards.pop() for x in range(number)]
            # if len(dealt) == 1:
            #     return dealt[0]  # Returns the single Card instance
            # else:
            return dealt[-number:]  # Returns list of Card instances

    def deal_card(self):
        return self._deal(1)[0]  # Need trick to add [0] to return Card not []. Saves if/else logic in _deal.

    def deal_hand(self, number):
        return self._deal(number)

my_deck = Deck()
my_deck.shuffle()
my_deck.reset()

for card in my_deck:
    print(card)



# d = Deck()
# print(d)
# print(d.cards)
# d.shuffle()
# print(d.cards)
# d.deal_hand(5)
# print(d.count())
# print(d.deal_card())


# c1 = Card('Diamonds', 4)
# c2 = Card('Hearts', 5)
#
# print(c1)
# print(c2.value)
#
# deck1 = Deck()
# print(deck1)
#
# print(deck1.cards[12].suit)  # Colt's solution just has deck[12].suit
#
# # print(deck1.count())
# print(len(deck1.cards))
# print(len(deck1))
# print(deck1.deal_hand(40))
# print(deck1.count())
# print(deck1.deal_hand(10))
# print(deck1.count())
# print(deck1.deal_card())
# print(deck1.count())
# print(deck1.deal_hand(2))
# print(deck1.count())




'''
Why not write the entire game in just one class?

Great question! Technically, you could write all programming logic for a massive game or app inside of a single class (or not even using a class at all).  So on one level, it's really just a nice way of organizing things into logical containers.  More specifically to the Card class...I know right now you could represent all the information in a card with a simple dictionary:

{"value": "A", "suit": "hearts"}
But by making it into a separate class, we could add way more functionality.  For example, what if we actually wanted each card to print out it's full name rather than just "Q", it should print "Queen of Hearts".  What if we wanted to add in functionality to compare cards to each other like:

card1 > card2
We could also add in error checking so that cards could only be created with valid suits and values.  Lastly, we can reuse the card class in any other card game we created.

So at the end of the day, you 100% can get away without using a Card class.  All of OOP is just a nice way of organizing your code.  It is never required to do anything, but it often can help make your code more readable and logical.



'''

'''
Colt's SOLUTION:

from random import shuffle
# Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)


class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __repr__(self):
		# return "{} of {}".format(self.value, self.suit)
		return f"{self.value} of {self.suit}"

# Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
# Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
# Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".
# Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck.
# Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck.

class Deck:
	def __init__(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
		self.cards = [Card(value, suit) for suit in suits for value in values]

	def __repr__(self):
		return f"Deck of {self.count()} cards"

	def count(self):
		return len(self.cards)

	def _deal(self, num):
		count = self.count()
		actual = min([count,num])
		if count == 0:
			raise ValueError("All cards have been dealt")
		cards = self.cards[-actual:]
		self.cards = self.cards[:-actual]
		return cards

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")

		shuffle(self.cards)
		return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()

# print(d.cards)

'''