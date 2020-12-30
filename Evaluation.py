"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 0.0
"""

import numpy as np

class Evaluation:

    def __init__(self):
        self.WINNING_COMBINATIONS = ([6,7,8], [3,4,5], [0,1,2],  # rows
                                     [6,3,0], [7,4,1], [8,5,2],  # columns
                                     [6,4,2], [8,4,0])           # diagonals

        self.player_arr = np.array([1,1,1]) # combination indicating player won
        self.opponent_arr = np.array([2,2,2]) # combination indicating opponent won


    def evaluate(self, game_state):
        game_arr = np.copy(game_state)
        player_won = False
        opponent_won = False
        tie = False

        # iterate over all game ending conditions
        for combination in self.WINNING_COMBINATIONS:
            # player already won
            if np.array_equal(game_arr[combination], self.player_arr):
                player_won = True
                break
            # opponent already won
            elif np.array_equal(game_arr[combination], self.opponent_arr):
                opponent_won = True
                break
        # no more turns possible
        if not len(game_arr[game_arr == 0]):
            tie = True

        return player_won, opponent_won, tie