def print_board(board):
    # Print the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check if the player has won in any row
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check if the player has won in any column
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check if the player has won in the main diagonal
    if all(board[i][i] == player for i in range(3)):
        return True
    # Check if the player has won in the anti-diagonal
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    # Check if the board is full (no empty spaces)
    return all(cell != ' ' for row in board for cell in row)

def main():
    # Initialize the board as a 3x3 grid of spaces
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        try:
            # Ask the current player for their move
            move = input(f"Player {current_player}, enter your move as row,col (0-2, e.g. 1,2): ")
            row, col = map(int, move.split(','))
            # Check if the chosen cell is already taken
            if board[row][col] != ' ':
                print("A vai tui late hoya geachis.")
                continue
        except (ValueError, IndexError):
            # Handle invalid input
            print("Invalid input, please enter row and column as numbers from 0 to 2.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        # Check if the board is full (tie)
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()