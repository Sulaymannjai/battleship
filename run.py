import random

# Creating the boad
BOARD_SIZE = 5
MAX_TURNS = 4
EMPTY = 'O'
HIT = 'X'
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Placeing the Ships
ship_row = random.randint(0, BOARD_SIZE - 1)
ship_col = random.randint(0, BOARD_SIZE - 1)

def print_board(board):
    """
    Welcome to My BattleShip
    """
    for row in board:
        print(" ".join(row))

def is_valid_input(row, col):
    return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

def play_battleship():
    print("Welcome to Battleship Game!")
    print_board(board)

    for turn in range(1, MAX_TURNS + 1):
        print("Turn", turn)
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if not is_valid_input(guess_row, guess_col):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == HIT:
            print("You guessed that one already.")
        elif guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!")
            board[guess_row][guess_col] = HIT
            break
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = HIT

        print("Current Board:")
        print_board(board)

        if turn == MAX_TURNS:
            print(
                "Game Over. The battleship was located at row",
                ship_row, "and column", ship_col
            )

if __name__ == "__main__":
    play_battleship()
