import random
import math  # Import the math module for infinity values

class Player:
    def __init__(self, letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # Randomly choose one of the available moves if it's the first move
            square = random.choice(game.available_moves())
        else:
            # Use the minimax algorithm to determine the best move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        """
        The minimax algorithm is a recursive function used to determine the best move 
        for the computer player. It simulates all possible moves and their outcomes 
        to find the optimal move.
        
        Parameters:
        state (TicTacToe): The current game state
        player (str): The current player's letter ('X' or 'O')

        Returns:
        dict: A dictionary containing the position and score of the best move
        """
        max_player = self.letter  # Yourself!
        other_player = 'O' if player == 'X' else 'X'

        # First, check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None,
                    'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)}
        elif not state.empty_squares():  # No empty squares (tie)
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Maximize score
        else:
            best = {'position': None, 'score': math.inf}  # Minimize score

        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # Simulate a game after making that move

            # Undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
