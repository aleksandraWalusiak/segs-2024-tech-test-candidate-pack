## Blackjack Game - Tech Test

This project implements a simple **Blackjack game** following object-oriented principles, with a focus on key components like the **Deck**, **Player**, **Hand**, and **Game** classes. The game includes mechanics for dealing cards, player actions (hit/stand), and determining the winner(s). It supports multiple players and handles various game scenarios such as busts and ties.

### Getting Started

- Ensure that you have Python 3 installed on your system.
  
- Clone or download the repository, and navigate to the folder containing the code. You should have the following files:
    - `deck.py`
    - `card.py`
    - `hand.py`
    - `player.py`
    - `game.py`
    - `play.py`
    - `test/` (containing unit tests)

- To run the Blackjack game:
    - Open the terminal, navigate to the folder containing the `blackjack.py` file.
    - Run the command `python3 blackjack.py` to start a game with 2 players (you can modify the number of players in the script).

- To run the tests:
    - Ensure the `test/` directory contains test files for the game logic.
    - In the terminal, navigate to the project folder and run `python3 -m unittest discover test` to execute the tests.

### Key Components

- **Deck**: Represents a deck of 52 cards, including functionality to shuffle and deal cards.
- **Card**: Represents a single card in the deck, with a rank and suit.
- **Hand**: Represents the collection of cards a player holds and calculates their hand's total value.
- **Player**: Represents a player in the game, with methods for taking actions (hit) and tracking if the player is bust.
- **Game**: Manages the game flow, handles player turns, determines the winner, and checks if the game is over.

### Game Flow

1. The game begins by dealing 2 cards to each player from the deck.
2. Players take turns where they can either:
    - **Hit** (draw a card from the deck)
    - **Stand** (end their turn and move to the next player)
3. If a player exceeds 21 points, they are **bust** and automatically lose.
4. The game ends once all players have either stood or busted. The winner is determined based on the highest total hand value (without exceeding 21).

### Example Game Run

```text
Player 1's turn
10 of Hearts, 7 of Diamonds
Total: 17
Enter 'hit' to draw a card or 'stand' to end your turn: hit
Player 1 drew a 5 of Clubs. Total is now 22.
Player 1 is bust!

Player 2's turn
10 of Spades, 6 of Hearts
Total: 16
Enter 'hit' to draw a card or 'stand' to end your turn: stand
Player 2 stands with a total of 16.

Game over!
Winner(s): Player 2 with a score of 16.
