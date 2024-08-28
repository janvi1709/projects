board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def print_board(board):
    print(*board[0], sep="  |  ")
    print("---------------")
    print(*board[1], sep="  |  ")
    print("---------------")
    print(*board[2], sep="  |  ")

def get_markers():
    while True:
        marker1 = input("Player 1 choice(X or O)").upper()
        if marker1 in ['X', 'O']:
            marker2 = 'O' if marker1 == 'X' else 'X'
            return [marker1, marker2]
        print("INVALID INPUT")

def get_coordinates():
    while True:
        r, c = map(int, input("Enter the coordinates: ").split())
        if r in [0, 1, 2] and c in [0, 1, 2]:
            return [r, c]
        print("INVALID INPUT")

def check_for_win(board):
    for row in board:
        if row[0] == row[1] and row[1] == row[2] and row[1] != " ":
            return True
    for i in range(len(board)):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != " ":
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] != " ":
        return True
    return False

def update_board(board, chance, marker, x, y):
    board[x][y] = marker
    if check_for_win(board):
        print_board(board)
        print(f"Player {1 if chance else 2} wins")
        return "Game Over"
    return not chance

def play_game():
    player1 = 0
    player2 = 0
    m1, m2 = get_markers()
    print(f"player1: {m1}, player2: {m2}")
    chances = True
    while True:
        print_board(board)
        x, y = get_coordinates()
        chances = update_board(board, chances, m1 if chances else m2, x, y)
        if chances == "Game Over":
            break

play_game()
