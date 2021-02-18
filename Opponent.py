"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 1.0
"""

import random
import numpy as np
from Evaluation import Evaluation

class Opponent:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.evaluation = Evaluation()


    def _alphabeta_search(self, game_state, depth, alpha, beta, is_maximizing):
        """ alpha-beta search """
        player_won, opponent_won, tie = self.evaluation.evaluate(game_state)

        if player_won:
            return -1 -1*depth # take depth into account
        elif opponent_won:
            return 1 + 1*depth # take depth into account
        elif tie or depth == 0:
            return 0

        if is_maximizing:
            value = float('-inf')
            # iterate over possible moves
            for empty_cell in np.where(game_state == 0)[0].tolist():
                # perform a possible move
                game_state[empty_cell] = 2
                # maximize the value
                value = max(value, self._alphabeta_search(game_state, depth-1, alpha, beta, not is_maximizing))
                # undo move from above
                game_state[empty_cell] = 0
                # maximize alpha
                alpha = max(alpha, value)
                # beta cutoff
                if alpha > beta:
                    break

            return value

        else:
            value = float('inf')
            # iterate over possible moves
            for empty_cell in np.where(game_state == 0)[0].tolist():
                # perform a possible move
                game_state[empty_cell] = 1
                # minimize the value
                value = min(value, self._alphabeta_search(game_state, depth-1, alpha, beta, not is_maximizing))
                # undo move from above
                game_state[empty_cell] = 0
                # minimize beta
                beta = min(beta, value)
                # alpha cutoff
                if beta <= alpha:
                    break

            return value


    def _minimax_ab(self, game_state, depth, alpha, beta):
        """ performs alpha-beta pruning """
        possible_moves = {}
        # iterate over possible moves
        for empty_cell in np.where(game_state == 0)[0].tolist():
            # perform a possible move
            game_state[empty_cell] = 2
            possible_moves[empty_cell] = self._alphabeta_search(game_state, depth, alpha, beta, False)
            # undo move from above
            game_state[empty_cell] = 0

        # return the index of the cell with the highest score
        return max(possible_moves, key=possible_moves.get)


    def next_turn(self, game_state):
        game_arr = np.copy(game_state)

        # ultra weak opponent
        # random choice without considering the score of a move
        if self.difficulty == 1:
            index = random.choice(np.where(game_arr == 0)[0].tolist())
            game_arr[index] = 2

        # reasonable opponent
        # alpha beta pruning with randomly performed bad moves
        elif self.difficulty == 2:
            index = self._minimax_ab(np.copy(game_arr), 4, -2, -2)
            # performs randomly bad moves by choosing a random move
            if random.choice([False, True, False]):
                index = random.choice(np.where(game_arr == 0)[0].tolist())
            game_arr[index] = 2

        # strong opponent
        # alpha beta pruning without any bad moves
        elif self.difficulty == 3:
            index = self._minimax_ab(np.copy(game_arr), 6, -2, 2)
            game_arr[index] = 2

        print(f"Your opponent's turn: {index+1}")

        return game_arr