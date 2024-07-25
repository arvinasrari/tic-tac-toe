
# Tic-Tac-Toe

This is a Python implementation of the classic Tic-Tac-Toe game. The game supports both human and computer players.

## Requirements

- Python 3.x

## Installation

Clone the repository and navigate to the project directory.

```bash
git clone https://github.com/arvinasrari/tic-tac-toe.git
cd tic-tac-toe
```

## Usage

Run the game using the following command:

```bash
python game.py
```

## Game Description

- The game is played on a 3x3 grid.
- Players take turns to place their marker (`X` or `O`) on an empty square.
- The first player to get 3 of their markers in a row (horizontally, vertically, or diagonally) wins.
- If all squares are filled and no player has 3 markers in a row, the game is a tie.

## Code Structure

- `game.py`: Contains the main game logic and the `TicTacToe` class.
- `player.py`: Contains the player classes (`HumanPlayer` and `SmartComputerPlayer`).

### `game.py`

This file includes:
- `TicTacToe` class: Manages the game board, moves, and determines the winner.
- `play` function: Controls the game flow, including player turns and move validation.

### `player.py`

This file includes:
- `HumanPlayer` class: Manages moves for human players.
- `RandomComputerPlayer` class: Manages moves for computer players making random moves.
- `SmartComputerPlayer` class: Manages moves for computer players using the minimax algorithm to choose the best move.

### Minimax Algorithm

The `SmartComputerPlayer` class uses the minimax algorithm to simulate all possible moves and their outcomes to find the optimal move. This algorithm ensures that the computer player makes the best possible move to win or tie the game.

## Example

```python
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = SmartComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please contact [Arvin Asrari](https://github.com/arvinasrari).
