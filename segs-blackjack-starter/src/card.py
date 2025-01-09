class Card:
    RANKS = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
    SUITS = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
    
    def __init__(self,rank, suit):
        self.rank = rank
        self.suit = suit
        self.val = self.assign_val()


    def assign_val(self):
        if self.rank in ('K', 'Q', 'J'):
            return 10
        elif self.rank == 'A':
            return 1
        else:
            return int(self.rank)