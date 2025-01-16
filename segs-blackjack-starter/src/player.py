class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.is_bust = False

    def hit(self, cards):
        self.hand.add_cards(cards)
        total = self.hand.calculate_total()
        if total > 21:
            self.is_bust = True 
        return total

    
