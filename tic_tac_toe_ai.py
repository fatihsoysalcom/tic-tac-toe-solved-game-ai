import random

# Represents the Tic-Tac-Toe board
board = [' '] * 9

# Player symbols
player_symbol = 'X'
computer_symbol = 'O'

def print_board(board):
    """Prints the current state of the board."""
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_available_moves(board):
    """Returns a list of indices of empty cells."""
    return [i for i, spot in enumerate(board) if spot == ' ']

def check_win(board, symbol):
    """Checks if the given symbol has won."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == symbol:
            return True
    return False

def minimax(board, depth, is_maximizing):
    """Minimax algorithm to find the best move for the computer."""
    if check_win(board, computer_symbol):
        return 1  # Computer wins
    if check_win(board, player_symbol):
        return -1 # Player wins
    if not get_available_moves(board):
        return 0  # Tie

    if is_maximizing:
        max_eval = -float('inf')
        for move in get_available_moves(board):
            board[move] = computer_symbol
            eval = minimax(board, depth + 1, False)
            board[move] = ' '  # Undo move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move] = player_symbol
            eval = minimax(board, depth + 1, True)
            board[move] = ' '  # Undo move
            min_eval = min(min_eval, eval)
        return min_eval

def get_computer_move(board):
    """Determines the computer's best move using Minimax."""
    best_eval = -float('inf')
    best_move = -1
    for move in get_available_moves(board):
        board[move] = computer_symbol
        eval = minimax(board, 0, False)
        board[move] = ' '  # Undo move
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

def get_player_move(board):
    """Gets the player's move from input."""
    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move in get_available_moves(board):
                return move
            else:
                print("Invalid move. That spot is taken or out of range.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """Main game loop."""
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Player's turn
        player_move = get_player_move(board)
        board[player_move] = player_symbol
        print_board(board)

        if check_win(board, player_symbol):
            print("Congratulations! You win!")
            break
        if not get_available_moves(board):
            print("It's a tie!")
            break

        # Computer's turn
        print("Computer is thinking...")
        computer_move = get_computer_move(board)
        board[computer_move] = computer_symbol
        print_board(board)

        if check_win(board, computer_symbol):
            print("Computer wins!")
            break
        if not get_available_moves(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
