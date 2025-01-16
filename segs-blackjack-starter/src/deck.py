import random
from src.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Card (rank, suit)
                self.cards.append(card)

    #Methods:
    #Shuffiling the deck ready to play
    def shuffle(self):
        random.shuffle(self.cards)

        
    #Deal (num of cards to deal)
    def deal(self, num):
        dealt_cards = []
        if len(self.cards) == 0 or num > len(self.cards):
            raise ValueError(f"Cannot deal {num} cards; only {len(self.cards)} cards available.")
        for _ in range(num):
            dealt_cards.append(self.cards.pop())
        return dealt_cards
        
