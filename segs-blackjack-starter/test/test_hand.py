import unittest
from src.deck import Deck
from src.hand import Hand

class HandTestCase(unittest.TestCase):
    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.hand = Hand()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_num_of_cards(self):
        dealt_cards = self.deck.deal(2)
        self.hand.add_cards(dealt_cards)
        number_of_cards = len(self.hand.cards)
        self.assertEqual(number_of_cards, 2)
    
    def test_total_number(self):
        dealt_cards = self.deck.deal(2)
        self.hand.add_cards(dealt_cards)
        sum = 0
        for card in self.hand.cards:
            sum = sum + card.val
        self.assertEqual(sum, self.hand.calculate_total())
