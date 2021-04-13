import utilities
import random
from random import randrange

lines = {
    0: [[4, 8], [1, 2], [3, 6]],
    1: [[0, 2], [4, 7]],
    2: [[4, 6], [0, 1], [5, 8]],
    3: [[4, 5], [0, 6]],
    4: [[2, 6], [0, 8], [3, 5], [1, 7]],
    5: [[3, 4], [2, 8]],
    6: [[2, 4], [7, 8], [0, 3]],
    7: [[6, 8], [1, 4]],
    8: [[0, 4], [6, 7], [2, 5]]
}


def get_player_move(player, board, player_symbols, computer_turn, difficulty):
    if computer_turn == player:
        boardmove = artificial_intelligence(
            board, player_symbols[player], player_symbols[player * -1], difficulty)
        return boardmove

    else:
        move_validation = False
        while not move_validation:
            move = input("What is your move? ")
            if move.isdigit():
                if int(move) > 0 and int(move) < 10:
                    move = int(move) - 1
                    if board[move] == " ":
                        board[move] = player_symbols[player]
                        break

            print("That is not a valid move. Please re-enter your move. ")

    return [board, move]


def artificial_intelligence(board, computer_symbol, player_symbol, difficulty):
    if difficulty == 1:
        move = randrange(0, 9)
        while board[move] != " ":
            move = randrange(0, 9)
        board[move] = computer_symbol
    if difficulty == 2:
        spots_to_take = []
        # check through the board to see what's in each spot
        for index in range(len(board)):
            # looks first for computer symbol
            if board[index] == computer_symbol:
                # looks through the possible winning lines
                for position in lines[index]:
                    # So long as neither spot in the line has an opponent spot, add the spots in this line to the spots_to_take consideration array
                    if board[position[0]] != player_symbol and board[position[1]] != player_symbol:
                        # return move if computer has an insta-win
                        if board[position[0]] == computer_symbol:
                            move = position[1]
                            board[move] = computer_symbol
                            return [board, move]
                        elif board[position[1]] == computer_symbol:
                            move = position[0]
                            board[move] = computer_symbol
                            return [board, move]
                    # if no insta-win, add the spots to consideration
                        else:
                            spots_to_take.append(position[0])
                            spots_to_take.append(position[1])
        for index in range(len(board)):
            if board[index] == player_symbol:
                # looks through possible losing lines
                for position in lines[index]:
                    # if computer has a symbol in the line skip it because it's not a winning line for the opponent. Otherwise proceed
                    if board[position[0]] != computer_symbol and board[position[1]] != computer_symbol:
                        # Block any insta-loss in position 1
                        if board[position[0]] == player_symbol:
                            if board[position[1]] == " ":
                                move = position[1]
                                board[move] = computer_symbol
                                return [board, move]
                        # Block any insta-loss in position 0
                        elif board[position[1]] == player_symbol:
                            if board[position[0]] == " ":
                                move = position[0]
                                board[move] = computer_symbol
                                return [board, move]
                        # if no insta-loss, still add it to consideration as a place to block
                        else:
                            spots_to_take.append(position[0])
                            spots_to_take.append(position[1])
        if len(spots_to_take) == 0:
            for spot_index in range(len(board)):
                if board[spot_index] == " ":
                    spots_to_take.append(spot_index)
            if len(spots_to_take) != 9:
                move = random.choice(spots_to_take)
                board[move] = computer_symbol
            else:
                if random.choice([1, 2]) == 1:
                    move = 4
                    board[move] = computer_symbol
                else:
                    move = random.choice([0, 2, 6, 8])
                    board[move] = computer_symbol
        else:
            count_hash = {4: 0}
            best_spot = 4
            for spot in spots_to_take:
                if spot in count_hash:
                    count_hash[spot] += 1
                else:
                    count_hash[spot] = 1
                if count_hash[spot] > count_hash[best_spot]:
                    best_spot = spot
            move = best_spot
            board[move] = computer_symbol

    return [board, move]


def game_end_check(turn, board, move, player, computer_turn):
    if turn > 4:
        for solutions in lines[move]:
            if board[move] == board[solutions[0]] and board[move] == board[solutions[1]]:
                if board[move] == "x":
                    board[move] = "X"
                    board[solutions[0]] = "X"
                    board[solutions[1]] = "X"
                else:
                    board[move] = "O"
                    board[solutions[0]] = "O"
                    board[solutions[1]] = "O"

                if computer_turn != 0:
                    if player == computer_turn:
                        print("Computer wins!")
                    else:
                        print("You win!")
                elif player == 1:
                    print("Player 1 wins!")
                elif player == -1:
                    print("Player 2 wins!")
                utilities.print_board(board)
                return False
        if turn == 9:
            utilities.print_board(board)
            print("Game over: tie")
            return False

    return True
