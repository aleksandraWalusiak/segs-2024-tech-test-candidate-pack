import unittest
from src.deck import Deck
from src.hand import Hand
from src.card import Card
from src.game import Game
from src.player import Player

class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.hand = Hand()
        player1_hand = Hand()
        player2_hand = Hand()
        self.player1 = Player("Rob", player1_hand)
        self.player2 = Player("Bob", player2_hand)
        self.game = Game([self.player1, self.player2], self.deck)

    def tearDown(self):
        pass

    def test_game_initialization(self):
        self.assertEqual(len(self.game.players), 2)
        self.assertEqual(self.game.current_turn, self.player1)
        self.assertFalse(self.game.game_over)

    def test_deal_initial_cards(self):
        self.game.deck.shuffle()
        for player in self.game.players:
            self.assertEqual(len(player.hand.cards), 2)

    def test_hit(self):
        initial_deck_size = len(self.deck.cards)
        self.game.current_turn.hit(self.deck.deal(1))
        self.assertEqual(len(self.game.current_turn.hand.cards), 3)
        self.assertEqual(len(self.deck.cards), initial_deck_size - 1)

    def test_stand(self):
        self.game.stand()
        self.assertEqual(self.game.current_turn, self.player2)
        self.assertFalse(self.game.game_over)

    def test_game_over(self):
        self.game.stand()
        self.game.stand()
        self.assertTrue(self.game.game_over)

    def test_winner_determined_correctly(self):
        self.player1.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.player2.hand.add_cards([Card('10', 'Clubs'), Card('6', 'Spades')])
        self.game.end_game()
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.players[0], self.player1)

    def test_tie_condition(self):
        self.player1.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.player2.hand.add_cards([Card('10', 'Clubs'), Card('7', 'Spades')])
        self.game.end_game()
        self.assertTrue(self.game.game_over)
        self.assertEqual(len(self.game.players), 2)

    def test_player_bust_after_hit(self):
        self.player1.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.game.player_hit()
        self.assertTrue(self.player1.is_bust)

    def test_player_not_bust_after_stand(self):
        self.player1.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.game.stand()
        self.assertFalse(self.player1.is_bust)

    def test_deck_depletion(self):
        self.deck.cards = []
        with self.assertRaises(ValueError):
            self.game.deck.deal(1)

    def test_player_cannot_action_after_bust(self):
        self.player1.hand.add_cards([Card('10', 'Hearts'), Card('7', 'Diamonds')])
        self.game.player_hit()
        self.game.player_hit()
        self.assertTrue(self.player1.is_bust)

    def test_multiple_rounds(self):
        self.game.stand()
        self.game.player_hit()
        self.assertEqual(len(self.player2.hand.cards), 3)
        self.assertEqual(self.game.current_turn, self.player2)
        self.game.stand()
        self.assertTrue(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
