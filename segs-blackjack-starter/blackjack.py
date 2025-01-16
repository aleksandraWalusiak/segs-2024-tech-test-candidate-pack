import time
from src.deck import Deck
from src.player import Player
from src.game import Game
from src.hand import Hand

def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)

def play():
    num_players = 2
    
    deck = Deck()
    deck.shuffle()
    
    players = []
    for i in range(num_players):
        hand = Hand()
        player = Player(f"Player {i + 1}", hand)
        players.append(player)
    
    game = Game(players, deck)

    while not game.game_over:
        print_with_delay(f"{game.current_turn.name}'s turn")
        print_with_delay(', '.join([f"{card.rank} of {card.suit}" for card in game.current_turn.hand.cards]))
        print_with_delay(f"Total: {game.current_turn.hand.calculate_total()}")
        
        action = input("Enter 'hit' to draw a card or 'stand' to end your turn: ").lower()
        
        if action == "hit":
            game.player_hit()
        elif action == "stand":
            game.stand()
        else:
            print_with_delay("Invalid action. Please enter 'hit' or 'stand'.", delay=1)

        print()

    print_with_delay("Game over!", delay=1)
    
    remaining_players = [player.name for player in game.players if not player.is_bust]
    if remaining_players:
        print_with_delay(f"Remaining players: {', '.join(remaining_players)}", delay=1)
    else:
        print_with_delay("All players have busted.", delay=1)

if __name__ == '__main__':
    play()
