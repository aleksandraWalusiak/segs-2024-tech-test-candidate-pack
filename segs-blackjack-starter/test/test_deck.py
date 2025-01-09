import unittest
from src.deck import Deck


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each test
        pass

    def test_number_of_cards(self):  # any method beginning with 'test_' will be run by unittest
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)

    def test_shuffle_deck(self):
        original_order = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)
        self.assertEqual(len(original_order), len(self.deck.cards))
        self.assertEqual(set(original_order), set(self.deck.cards))

    def test_deal_cards(self):
        dealt_cards = self.deck.deal(5)
        self.assertEqual(len(dealt_cards), 5)
        self.assertEqual(len(self.deck.cards), 47)

    def test_deal_more_than_in_deck(self):
        with self.assertRaises(ValueError, msg="Should raise an error if more cards are requested than available"):
            self.deck.deal(60)
        self.assertEqual(len(self.deck.cards), 52)


    def test_deal_empty_deck(self):
        self.deck.deal(52)  # Empty the deck
        with self.assertRaises(ValueError, msg="Should raise an error if more cards are requested than available"):
            self.deck.deal(1)

    def test_check_deck_valid(self):
        """Test that the deck contains all the correct cards with the correct values."""
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        rank_values = {
            '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
            'J': 10, 'Q': 10, 'K': 10, 'A': 1
        }

        # Generate the expected set of cards
        expected_cards = {(rank, suit, rank_values[rank]) for suit in suits for rank in ranks}

        # Get the actual set of cards from the deck
        actual_cards = {(card.rank, card.suit, card.val) for card in self.deck.cards}

        self.assertEqual(
            actual_cards,
            expected_cards,
            "The deck should contain all 52 cards with correct values."
        )


if __name__ == '__main__':
    unittest.main()
