class Game:
    def __init__(self, players, deck):
        self.players = players
        self.current_turn = players[0]
        self.deck = deck
        self.game_over = False

        for player in self.players:
            player.hand.add_cards(self.deck.deal(2))
            player.has_acted = False
            player.is_bust = False

    def player_hit(self):
        if self.current_turn.is_bust:
            print(f"{self.current_turn.name} is bust! No more actions allowed.")
            return

        card = self.deck.deal(1)
        total = self.current_turn.hit(card)
        print(f"{self.current_turn.name} drew a {card[0].rank} of {card[0].suit}. Total is now {total}.")

        if self.current_turn.is_bust:
            print(f"{self.current_turn.name} is bust!")
            self.next_turn()
        else:
            print(f"{self.current_turn.name}'s total is now {total}.")

    def stand(self):
        print(f"{self.current_turn.name} stands with a total of {self.current_turn.hand.calculate_total()}.")
        self.current_turn.has_acted = True
        self.next_turn()

    def next_turn(self):
        if all(player.has_acted or player.is_bust for player in self.players):
            self.end_game()
            return

        current_index = self.players.index(self.current_turn)
        next_index = (current_index + 1) % len(self.players)

        while self.players[next_index].has_acted or self.players[next_index].is_bust:
            next_index = (next_index + 1) % len(self.players)
            if next_index == current_index:
                self.end_game()
                return

        self.current_turn = self.players[next_index]
        print(f"{self.current_turn.name}'s turn now.")

    def end_game(self):
        self.game_over = True
        print("Game over!")

        remaining_players = [player for player in self.players if not player.is_bust]
        if remaining_players:
            max_score = max(player.hand.calculate_total() for player in remaining_players)
            winners = [player.name for player in remaining_players if player.hand.calculate_total() == max_score]
            print(f"Winner(s): {', '.join(winners)} with a score of {max_score}.")
        else:
            print("All players are bust. No winners.")
