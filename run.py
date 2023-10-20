import random

# Creating the board
board_size = 10
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

# Putting the ships
ship_row = random.randint(0, board_size - 1)
ship_col = random.randint(0, board_size - 1)

# Receiving your imputs
for _ in range(4): 
    print("Turn", _ + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))


print("Current Board:")