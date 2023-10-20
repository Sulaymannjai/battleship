import random

# Creating the board
board_size = 10
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

# Putting the ships
ship_row = random.randint(0, board_size - 1)
ship_col = random.randint(0, board_size - 1)

