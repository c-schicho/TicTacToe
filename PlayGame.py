"""
Author: Christopher Schicho
Project: Tic-Tac-Toe
Version: 0.0
"""

from TicTacToe import TicTacToe

if __name__ == "__main__":
    print("\033[91m#######################\033[0m")
    print("\033[91m***** Tic-Tac-Toe *****\033[0m")
    print("\033[91m#######################\033[0m")
    print("\033[33mby Christopher Schicho\033[0m\n")
    print("In order to make it easier to remember the corresponding number for each cell, I decided to use")
    print("the same scheme as the number pad of your keyboard. Below you can see the corresponding numbers.\n")
    print("""\t-------------------
        | (7) | (8) | (9) |
        -------------------
        | (4) | (5) | (6) |
        -------------------
        | (1) | (2) | (3) |
        -------------------\n""")

    print("The player who is allowed to start is going to be chosen randomly.\n")
    print("Choose the level of your opponent from the interval of 1 to 3,")
    print("1 means weak and 3 means strong. Enter only integers.")

    input_valid = False
    while not input_valid:
        difficulty = input("Enter your Input [1-3]: ")
        try:
            difficulty = int(difficulty.strip())
            if 0 < difficulty <= 3:
                input_valid = True
            else:
                raise ValueError
        except ValueError:
            print("\033[91mERROR:\033[0m the entered input is invalid!")

    # start the game
    TicTacToe(difficulty).run_game()