""" Full coverage testing for deck and card classes. Meaning need to have
tests for all functions within both classes. Refer to card.py and deck.py.

Testing ideas: tests: __init__, __repr__, deal_sufficient, deal_insufficient, 
no_cards, deal_card, deal_hand, deal_shuffle (something changed/order changed)

Colt put all the testing in one with separate CardTests and DeckTests classes.

Questions that come up while working through this:
-Should I combine CardTests init valid/invalid functions?
-What's the point of msg= for assert tests? Doesn't the triple-double do that?
-Should I create separate Deck()s other than just the one single setUp() deck?
    - If I want to test out a deck with 0 cards, I first have to deal. Better way?
-Don't need to reimport random choice again since I've imported deck, right?
-If accessing cards in a deck, can I just use self.deck? Or must add self.deck.cards?
    -A: Gotta use self.deck.cards I think.


**You need to TEST THE ACTUAL FUNCTION! If testing __repr__ then call repr()!!!


Additional resources:
https://docs.python.org/3/library/unittest.html#skipping-tests-and-expected-failures
http://melp.nl/2011/02/enhancing-python-unit-tests-with-more-decorators/


"""
import unittest
from card import Card
from deck import Deck


class CardTests(unittest.TestCase):

    def setUp(self):
        self.card = Card("Hearts", "A")
        # self.X_of_Wrong = Card("Wrong", "X") - not needed? - NOT ideal
        
    def test_init_valid(self):  # Should I combine valid/invalid?
        """__init__ should set suit and value if valid"""
        self.assertIn(self.card.suit, Card.available_suits)
        self.assertIn(self.card.value, Card.available_values)
        # Colt. Checking the suit and value match
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")
    
    def test_init_invalid(self):
        """__init__ should raise ValueError if suit is invalid"""
        # self.X_of_Wrong = Card("Wrong", "X") - not needed?
        with self.assertRaises(ValueError):
            Card("Wrong", "A")  # Can you do this?
        with self.assertRaises(ValueError):
            Card("Hearts", "X")

    def test_repr(self):
        """__repr__ should return a string {value} of {suit}"""
        self.assertEqual(repr(self.card), "A of Hearts")
        # Alternative syntax:
        # self.assertEqual(self.card.__repr__(), "A of Hearts")


class DeckTests(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        
    def test_init(self):
        """__init__ should create a deck/list of 52 cards"""
        self.assertEqual(len(self.deck.cards), 52)
        self.assertIsInstance(self.deck.cards, list)
        # Colt's
        # self.assertTrue(isinstance(self.deck.cards, list))

    def test_repr(self):
        """__repr__ returns 'Deck of {self.count()} cards'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")
    
    def test_reset(self):
        """Should reset back to init state"""
        self.assertEqual(self.deck, self.deck.reset())

    def test_shuffle_insufficient(self):
        """Only shuffle decks of 52 cards"""
        # How to properly call shuffle()? Deck.shuffle()? self.deck.shuffle(self.deck.cards)?
        # self.assertSequenceEqual(self.deck.cards, Deck.shuffle(self.deck.cards))
        # Keep getting != <bound method Deck.shffle of Deck of 52 cards>

        # Broken: self.assertEqual(self.deck.cards[0:5], self.deck.shuffle())
        self.deck.deal_card()
        with self.assertRaises(ValueError):
            # Deck.shuffle(self.deck)
            self.deck.shuffle()
    
    # Colt's shuffle full deck solution
    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]  # A way to copy original state
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)  # This is key since [] != full deck

    # Colt tested the _deal method directly. Here's his tests:
    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    # Colt's. Similar to my _insufficient below
    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    # Colt's test for ValueError
    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        self.deck._deal(self.deck.count()) # clever way to deal all/empty the deck
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    
    def test_deal_card_insufficient(self):
        """Should deal all remaining cards or raise ValueError when zero cards left"""
        # First dealing out all cards. 
        self.assertEqual(self.deck.cards[-self.deck.count()::], self.deck.deal_hand(53)[::-1])
        # Then trying to deal single card when no cards left (self.deck.count() = 0)
        with self.assertRaises(ValueError):
            self.deck.deal_card()
    
    def test_deal_card(self):
        """Subtracts 1 card from deck and returns card instance"""
        # swap order so [-1] gets retrieved before deal pops() card
        # if going to call deal_card() directly, need to place at top to get count of 51
        self.deck.deal_card()
        self.assertEqual(self.deck.count(), 51)
        self.assertEqual(self.deck.cards[-1], self.deck.deal_card())
        # if using assertNotIn, can I just use self.deck? Seems that way...
        self.assertNotIn(self.deck.deal_card(), self.deck, msg="Once dealt, the card shouldn't be in original deck")
        # Colt's solution. Nice use of variables (card and dealt_card)
        # card = self.deck.cards[-1]
        # dealt_card = self.deck.deal_card()
        # self.assertEqual(card, dealt_card)
        # self.assertEqual(self.deck.count(), 51)
        
    def test_deal_hand(self):
        """Cards should be dealt from the top (end) of the deck"""
        self.assertEqual(self.deck.cards[-6::], self.deck.deal_hand(6)[::-1])
        # Colt's solution.
        # cards = self.deck.deal_hand(20)
        # self.assertEqual(len(cards), 20)
        # self.assertEqual(self.deck.count(), 32)
        
    def test_count(self):
        """Return the number of cards in Deck.cards"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.deal_hand(10)
        # Colt's using pop() then checking count() = 51
        # self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 42)







if __name__ == "__main__":
    unittest.main()
