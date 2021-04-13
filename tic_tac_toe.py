import utilities
import gameplay
from random import random

clear = "\n" * 100
computer_turn = 0
difficulty = 1
player_symbols = ["", "x", "o"]

print(clear)
print("Welcome to Tic Tac Toe!")
print("Do you want to play a friend or the computer? Enter the number of your selection.")
print("1) vs. Computer")
print("2) vs. Friend")
num_players = input()

while num_players != "1" and num_players != "2":
    print("That is not a valid input. Please re-enter your selection or enter q to quit.")
    num_players = input()
    if num_players[0] == "q" or num_players == "Q":
        print("Goodbye.")
        quit()
if num_players == "2":
    print("You have chosen to play a friend.")
else:
    print("You are playing the computer.")
    difficulty = utilities.choose_difficulty()
    computer_turn = -1

utilities.print_positions()
print("On your turn, enter the number of your chosen position.")
input("Press enter to continue. ")

keep_playing = True

while keep_playing:
    continue_game = True
    turn = 0
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    board_and_move = [board]
    player = -1
    if random() > 0.5:
        player_symbols = ["", "o", "x"]

    if computer_turn != 0:
        if random() > 0.5:
            print("The computer has been randomly chosen to go first.")
            accept = input("Do you accept? (y/n) ")
            if accept == "y" or accept == "Y":
                computer_turn = 1
                print("Accepted.")
            else:
                print("You will go first.")
        else:
            computer_turn = -1

        print()
        print("Your symbol is " + player_symbols[-1 * computer_turn] + ".")
        print("The computer's symbol is " +
              player_symbols[computer_turn] + ".")
        if computer_turn == 1:
            input("Press enter to continue. ")
    else:
        print()
        print("Player 1 is " + player_symbols[1] + ".")
        print("Player 2 is " + player_symbols[2] + ".")

    while continue_game:
        player = player * -1

        utilities.print_board(board_and_move[0])

        board_and_move = gameplay.get_player_move(
            player, board, player_symbols, computer_turn, difficulty)
        turn += 1

        print(clear)

        continue_game = gameplay.game_end_check(
            turn, board_and_move[0], board_and_move[1], player, computer_turn)

    print("Play again? (y/n)")
    keep_playing = input()
    if keep_playing:
        if keep_playing[0] == "n" or keep_playing[0] == "N":
            print("Goodbye!")
            quit()

    keep_playing = True
    if computer_turn != 0:
        difficulty = utilities.choose_difficulty()
