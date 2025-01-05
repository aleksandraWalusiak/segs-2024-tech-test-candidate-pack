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
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Generate the expected set of cards
        expected_cards = {f"{rank} of {suit}" for suit in suits for rank in ranks}

        # Get the actual set of cards from the deck
        actual_cards = {f"{card.rank} of {card.suit}" for card in self.deck.cards}

        self.assertEqual(
            actual_cards,
            expected_cards
        )




if __name__ == '__main__':
    unittest.main()
