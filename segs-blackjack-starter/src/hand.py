class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards1):
        for card in cards1:
            self.cards.append(card)

    def calculate_total(self):
        total = sum(card.val for card in self.cards)
        ace_count = sum(1 for card in self.cards if card.rank == 'A')
        while ace_count > 0 and total + 10 <= 21:
            total += 10
            ace_count -= 1

        return total
