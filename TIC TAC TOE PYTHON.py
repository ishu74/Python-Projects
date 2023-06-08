def print_board(board):
    print("---------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" ")
            print("|", end=" ")
        print("\n---------")

def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)

        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

play_game()
