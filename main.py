# Function to print the board
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")


# Function to check if a player has won
def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
                        (0, 4, 8), (2, 4, 6)]  # Diagonal

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False


# Function to check if the board is full (Draw condition)
def is_board_full(board):
    return "_" not in board


# Function to play the game
def play_game():
    board = ["_" for _ in range(9)]  # Create an empty board
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Get the player's move
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if board[move] != "_":
                print("That position is already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")
            continue

        # Make the move
        board[move] = current_player
        print_board(board)

        # Check if the current player won
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if is_board_full(board):
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Run the game
if __name__ == "__main__":
    play_game()
