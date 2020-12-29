"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 0.0
"""

import random
import numpy as np
from Evaluation import Evaluation
from Opponent import Opponent

class TicTacToe:

    def __init__(self, difficulty):
        self.evaluation = Evaluation()
        self.opponent = Opponent(difficulty)
        self.starting_player = random.choice([1, 2]) # 1=player 2=opponent
        self.SIGN_PLAYER = "\033[91mO\033[0m"
        self.SIGN_OPPONENT = "\033[94mX\033[0m"
        self.game_arr = np.zeros(9, dtype=np.int)
        self.WINNING_COMBINATIONS = ([6,7,8], [3,4,5], [0,1,2],  # rows
                                     [6,3,0], [7,4,1], [8,5,2],  # columns
                                     [6,4,2], [8,4,0])           # diagonals
        self.player_arr = np.array([1,1,1])
        self.opponent_arr = np.array([2,2,2])
        self.player_won = False
        self.opponent_won = False
        self.tie = False


    def __str__(self):
        # convert array data type to string
        str_arr = np.copy(self.game_arr).astype(str)

        # replace representations
        str_arr[str_arr == "0"] = " "
        str_arr[str_arr == "1"] = self.SIGN_PLAYER
        str_arr[str_arr == "2"] = self.SIGN_OPPONENT

        game_string = f"""\n\t-------------
        | {str_arr[6]} | {str_arr[7]} | {str_arr[8]} |
        -------------
        | {str_arr[3]} | {str_arr[4]} | {str_arr[5]} |
        -------------
        | {str_arr[0]} | {str_arr[1]} | {str_arr[2]} |
        -------------\n"""

        return game_string


    def _next_turn_(self, game_state):
        game_arr = np.copy(game_state)

        input_valid = False
        while not input_valid:
            player_input = input("It's your turn, enter the number corresponding to the cell you want to fill [1-9]: ")
            try:
                player_input = int(player_input)
                if 0 < player_input <= 9 and not game_arr[player_input - 1]:
                    game_arr[player_input-1] = 1
                    input_valid = True
                else:
                  raise ValueError
            except ValueError:
                print("\033[91mERROR:\033[0m the entered input is invalid!")
        return game_arr


    def run_game(self):
        # set order of players
        if self.starting_player == 1:
            player1 = self
            player2 = self.opponent
            print("\nYou are going to start")
        else:
            player1 = self.opponent
            player2 = self
            print("\nYour opponent is going to start.")

        # run game
        while not self.player_won and not self.opponent_won and not self.tie:
            self.game_arr = player1._next_turn_(self.game_arr)
            print(self)
            self.player_won, self.opponent_won, self.tie = self.evaluation.evaluate(self.game_arr)

            if self.player_won or self.opponent_won or self.tie:
                # end the game loop
                break

            self.game_arr = player2._next_turn_(self.game_arr)
            print(self)
            self.player_won, self.opponent_won, self.tie = self.evaluation.evaluate(self.game_arr)

        # end of the game
        if self.player_won:
            print("Awesome, you won the game!")
        elif self.opponent_won:
            print("Your opponent won, maybe you choose a weaker one!")
        else:
            print("The game ended with a tie!")

        print("\nI hope you enjoyed the game!")