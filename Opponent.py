"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 0.0
"""

import random
import numpy as np

class Opponent:

    def __init__(self, difficulty):
        self.difficulty = difficulty


    def _next_turn_(self, game_arr):
        # only for testing
        print("Your opponent's turn:")
        game_arr = np.array(game_arr, dtype=np.int)
        turn = random.choice(np.where(game_arr == 0)[0].tolist())
        game_arr[turn] = 2
        return game_arr