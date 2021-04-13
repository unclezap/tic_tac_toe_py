# from random import randrange

def print_board(board_list):
    print('''
   {} | {} | {}
  -----------
   {} | {} | {}
  -----------
   {} | {} | {}
   '''.format(*board_list))

def print_positions():
    print_board(range(1,10))

def choose_difficulty():
    print("What difficulty level would you like to play?")
    print("1) Beginner")
    print("2) Advanced")
    difficulty_validation = False
    while not difficulty_validation:
        difficulty = input("Enter the number of your selection. ")
        if difficulty.isdigit():
            if int(difficulty) > 0 and int(difficulty) < 3:
                difficulty = int(difficulty)
                break 
        print("That is not a valid selction. Please re-enter your difficulty level.")
    return difficulty