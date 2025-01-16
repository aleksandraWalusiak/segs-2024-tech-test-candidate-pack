import unittest
from src.deck import Deck
from src.hand import Hand
from src.card import Card

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
    
    def test_total_number_random(self):
        dealt_cards = self.deck.deal(2)
        
        self.hand.add_cards(dealt_cards)
        
        calculated_sum = 0
        ace_count = 0
        for card in self.hand.cards:
            if card.rank == 'A':
                ace_count += 1
            else:
                calculated_sum += card.val

        while ace_count > 0:
            if calculated_sum + 11 <= 21:
                calculated_sum += 11
            else:
                calculated_sum += 1
            ace_count -= 1

        self.assertEqual(
            calculated_sum,
            self.hand.calculate_total(),
            f"Expected total {calculated_sum}, but got {self.hand.calculate_total()}."
        )

    # ---------------- Required Tests -------------------------

    def test_valid_hand_when_score_21_or_less(self):
        self.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.assertTrue(self.hand.calculate_total() <= 21)

    def test_bust_hand_when_score_22_or_more(self):
        self.hand.add_cards([Card('10', 'Hearts'), Card('10', 'Diamonds'), Card('5', 'Clubs')])
        self.assertTrue(self.hand.calculate_total() > 21)

    def test_king_and_ace_score_21(self):
        self.hand.add_cards([Card('K', 'Hearts'), Card('A', 'Diamonds')])
        self.assertEqual(self.hand.calculate_total(), 21)

    def test_king_queen_and_ace_score_21(self):
        self.hand.add_cards([Card('K', 'Hearts'), Card('Q', 'Diamonds'), Card('A', 'Clubs')])
        self.assertEqual(self.hand.calculate_total(), 21)

    def test_nine_and_two_aces_score_21(self):
        self.hand.add_cards([Card('9', 'Spades'), Card('A', 'Diamonds'), Card('A', 'Hearts')])
        self.assertEqual(self.hand.calculate_total(), 21)


