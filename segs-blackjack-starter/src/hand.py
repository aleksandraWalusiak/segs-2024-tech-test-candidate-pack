class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    def calculate_total(self):
        pass
