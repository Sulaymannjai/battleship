import random

# Creating the board
board_size = 5
board = [['O' for _ in range(board_size)] for _ in range(board_size)]

# Putting the ships
ship_row = random.randint(0, board_size - 1)
ship_col = random.randint(0, board_size - 1)

# Receiving your imputs
for _ in range(1, 5):

    print("Turn", _ + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Conratutations!! you sunk my battleship")
        break
else:
    if guess_row not in range(board_size) or guess_col not in range(board_size):
        print("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == 'X':
        print("You guessed that one already.")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = 'X'

print("Current Board:")
for row in board:
    print(" ".join(row))

if _ == 4:
    print(
        "Game Over. The battleship was located at row",
        ship_row, "and column", ship_col
        )
