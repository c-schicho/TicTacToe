"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 0.0
"""

import random
import numpy as np
from Evaluation import Evaluation

class Opponent:

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.evaluation = Evaluation()


    def __alphabeta_search__(self, game_state, depth, alpha, beta, is_maximizing):
        player_won, opponent_won, tie = self.evaluation.evaluate(game_state)

        if player_won:
            return -1 -1*depth
        elif opponent_won:
            return 1 + 1*depth
        elif tie or depth == 0:
            return 0

        if is_maximizing:
            value = float('-inf')
            for empty_cell in np.where(game_state == 0)[0].tolist():
                game_state[empty_cell] = 2
                value = max(value, self.__alphabeta_search__(game_state, depth-1, alpha, beta, not is_maximizing))
                game_state[empty_cell] = 0
                alpha = max(alpha, value)
                # beta cutoff
                if alpha > beta:
                    break
            return value

        else:
            value = float('inf')
            for empty_cell in np.where(game_state == 0)[0].tolist():
                game_state[empty_cell] = 1
                value = min(value, self.__alphabeta_search__(game_state, depth-1, alpha, beta, not is_maximizing))
                game_state[empty_cell] = 0
                beta = min(beta, value)
                # alpha cutoff
                if beta <= alpha:
                    break
            return value


    def __minimax_ab__(self, game_state, depth, alpha, beta):
        possible_moves = {}
        for empty_cell in np.where(game_state == 0)[0].tolist():
            game_state[empty_cell] = 2
            possible_moves[empty_cell] = self.__alphabeta_search__(game_state, depth, alpha, beta, False)
            game_state[empty_cell] = 0

        return max(possible_moves, key=possible_moves.get)



    def _next_turn_(self, game_state):
        game_arr = np.copy(game_state)

        # ultra weak opponent
        # random choice without considering the score of a move
        if self.difficulty == 1:
            index = random.choice(np.where(game_arr == 0)[0].tolist())
            game_arr[index] = 2

        # reasonable opponent
        # alpha beta pruning with randomly performed bad moves
        elif self.difficulty == 2:
            index = self.__minimax_ab__(np.copy(game_arr), 4, -2, -2)
            if random.choice([False, True, False]):
                index = random.choice(np.where(game_arr == 0)[0].tolist())
            game_arr[index] = 2

        # strong opponent
        # alpha beta pruning
        elif self.difficulty == 3:
            index = self.__minimax_ab__(np.copy(game_arr), 6, -2, 2)
            game_arr[index] = 2

        print(f"Your opponent's turn: {index+1}")

        return game_arr