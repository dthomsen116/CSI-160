import time
import replit


# Constants in are named in all caps (PEP8 Standard)
PLAYER_X = 'x'

PLAYER_O = 'o'

EMPTY = ' '

TIE_GAME = 'Tie'

BOARD_SIZE = 3

# Player X goes first
current_player = PLAYER_X

# Builds an EMPTY board
board = [[EMPTY, EMPTY, EMPTY],
        [EMPTY,  EMPTY, EMPTY],
        [EMPTY,  EMPTY, EMPTY]]


def print_board():
    # Clear the screen
    replit.clear()

    # Prints the board to the console

    print('    0   1   2')
    print('  -------------')
    for i, row in enumerate(board):
        print(i, end="")
        for square in row:
            print(' | ' + square, end="")
        print(' |')
        print('  -------------')


def is_empty(row, col):
    """Returns True/False if a square is EMPTY

    params row, col: (int) The row and Column to Check
    return: (boolean) If the row is EMPTY
    """
    # TODO Part #1 complete is_EMPTY()
    if board[row][col] == EMPTY:
        return True
    else:
        return False


def move(player, row, col):
    """Makes a game move

    If a move is legal, moves the player to the row and col
    and returns True. If a move is illegal, no move is made
    and returns False. Hint: Should make use of is_empty()

    param player: Either PLAYER_X or PLAYER_O
    param row, col: (int) The row and Column to move to
    return: (boolean) Success of the move
    """
    # TODO Part #2 complete move()
    board[row][col] = player


def determine_winner():
    """Determine if there is a winner

    return: Returns None if there is no winner.
            Returns PLAYER_O or PLAYER_X if one of them won.
            Returns 'tie' if noone wins
    """


    # TODO Part #3 complete determine_winner()
# Step 1: Check the horizontals looking for a winner.
    #         If so return winner.
    for row in (0,1,2):
        if board[row][0] and board[row][1] and board[row][2] == PLAYER_X:
            row = row + 1
            return current_player

    # Step 2: Check the verticals looking for a winner
    #         If so return winner.
    for col in (0,1,2):
        if board[col][0] == board[col][1] == board[col][2] == PLAYER_X:
            col = col + 1
            return current_player

    # Step 3: Check the diagonals looking for a winner
    #         If so return winner.

    # Step 4: Check to see if there are empty squares.
    #         If there are empty squares, return None because
    #         no one has won the game yet
    #         If there are no empty squares return TIE_GAME
    #         because we didn't find a winner and all moves are made
    for row_num in (0, 1, 2):
        for col_num in (0, 1, 2):
            if is_empty(row_num, col_num): # If the space is empty return none
                return None

    return TIE_GAME


while True:
    print()
    print_board()
    print()
    print('It is', current_player, "'s turn")
    row = int(input('Row (0-2)? '))
    col = int(input('Column (0-2)? '))

    # Make sure the move is legal, if so make the move
    if is_empty(row, col):
        move(current_player, row, col)
    else:
        print('You cannot do that.')
        time.sleep(1)
        continue

    # Check if there is a winner
    winner = determine_winner()
    if winner in (PLAYER_O, PLAYER_X):
        print_board()
        print(winner,' Is the winner!')
        break

    if winner == TIE_GAME:
        print_board()
        print("The game is a draw.")
        break

    # Let the other player have a turn
    if current_player == PLAYER_O:
        current_player = PLAYER_X
    else:
        current_player = PLAYER_O
