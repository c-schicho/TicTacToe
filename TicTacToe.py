"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 1.0
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
        self.SIGN_PLAYER = "\033[91mO\033[0m" # O
        self.SIGN_OPPONENT = "\033[94mX\033[0m" # X
        self.game_arr = np.zeros(9, dtype=np.int)
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


    def next_turn(self, game_state):
        """ performs move of the human player """
        game_arr = np.copy(game_state)

        input_valid = False
        while not input_valid:
            player_input = input("It's your turn, enter the number corresponding to the cell you want to fill [1-9]: ")
            # check validity of players input
            try:
                player_input = int(player_input)
                if 0 < player_input <= 9 and not game_arr[player_input - 1]:
                    # perform players move
                    game_arr[player_input-1] = 1
                    input_valid = True
                else:
                  raise ValueError
            except ValueError:
                print("\033[91mERROR:\033[0m the entered input is invalid!")
        return game_arr


    def run_game(self):
        """ game loop """
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
            # player1's turn
            self.game_arr = player1.next_turn(self.game_arr)
            print(self)
            self.player_won, self.opponent_won, self.tie = self.evaluation.evaluate(self.game_arr)

            # check if the last turn resulted in a game ending condition
            if self.player_won or self.opponent_won or self.tie:
                # end the game loop
                break

            # player2's turn
            self.game_arr = player2.next_turn(self.game_arr)
            print(self)
            self.player_won, self.opponent_won, self.tie = self.evaluation.evaluate(self.game_arr)

        # evaluate end of the game
        if self.player_won:
            print("Awesome, you won the game!")
        elif self.opponent_won:
            print("Your opponent won, maybe you choose a weaker one!")
        else:
            print("The game ended with a tie!")

        print("\nI hope you enjoyed the game!")