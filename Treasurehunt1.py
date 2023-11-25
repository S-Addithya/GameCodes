import random

def create_board(rows, cols):
    return [[' ' for _ in range(cols)] for _ in range(rows)]

def place_treasure(board):
    treasure_row = random.randint(0, len(board) - 1)
    treasure_col = random.randint(0, len(board[0]) - 1)
    board[treasure_row][treasure_col] = 'X'
    return treasure_row, treasure_col

def print_board(board):
    for row in board:
        print(' '.join(row))

def get_player_move():
    try:
        row = int(input('Enter row (0 to {}): '.format(len(board) - 1)))
        col = int(input('Enter column (0 to {}): '.format(len(board[0]) - 1)))
        return row, col
    except ValueError:
        print('Invalid input. Please enter numbers.')
        return get_player_move()

def play_game(board, max_attempts):
    treasure_row, treasure_col = place_treasure(board)
    attempts = 0

    while attempts < max_attempts:
        print_board(board)
        player_row, player_col = get_player_move()

        if player_row == treasure_row and player_col == treasure_col:
            print('Congratulations! You found the treasure!')
            break
        else:
            print('Oops! Not here. Keep searching.')
            attempts += 1

    if attempts == max_attempts:
        print('Sorry, you ran out of attempts. The treasure was at row {} and column {}.'.format(treasure_row, treasure_col))

if __name__ == "__main__":
    rows = 5
    cols = 5
    max_attempts = 10

    board = create_board(rows, cols)
    print("Welcome to the Treasure Hunting Game!")
    play_game(board, max_attempts)
