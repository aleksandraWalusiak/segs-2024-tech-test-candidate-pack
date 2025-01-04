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
        if len(self) == 0:
            return None
        else:
            for _ in range(num):
                self.cards.pop()
        
