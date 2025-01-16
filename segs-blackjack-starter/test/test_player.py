import unittest
from src.deck import Deck
from src.hand import Hand
from src.card import Card
from src.player import Player

class PlayerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
        self.hand = Hand()
        self.player = Player("Rob", self.hand)

    def tearDown(self):
        pass

    def test_player_initialization(self):
        self.assertEqual(self.player.name, "Rob")
        self.assertEqual(len(self.player.hand.cards), 0)
        self.assertFalse(self.player.is_bust)

    def test_player_hit(self):
        self.player.hit([Card('5', 'Hearts')])
        self.assertEqual(len(self.player.hand.cards), 1)
        self.assertEqual(self.player.hand.cards[0].rank, '5')
        
    def test_player_bust_after_hit(self):
        self.player.hit([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.player.hit([Card('5', 'Clubs')])
        self.assertTrue(self.player.is_bust)

    def test_player_hand_total(self):
        self.player.hit([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.assertEqual(self.player.hand.calculate_total(), 17)
        self.player.hit([Card('4', 'Clubs')])
        self.assertEqual(self.player.hand.calculate_total(), 21)

    def test_player_not_bust_before_exceeding_21(self):
        self.player.hit([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.assertFalse(self.player.is_bust)
        self.player.hit([Card('5', 'Clubs')])
        self.assertTrue(self.player.is_bust)

    def test_player_can_hit_multiple_times(self):
        self.player.hit([Card('2', 'Hearts')])
        self.player.hit([Card('3', 'Diamonds')])
        self.player.hit([Card('5', 'Spades')])
        self.player.hit([Card('3', 'Spades')])
        self.assertEqual(len(self.player.hand.cards), 4)
        self.assertEqual(self.player.hand.calculate_total(), 13)

if __name__ == '__main__':
    unittest.main()
