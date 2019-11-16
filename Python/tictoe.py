board = [
    ['x', 'o', ' ']
    ['o', 'o', 'x']
    ['x', 'o', ' ']
]
def check_win(board):
    for row in board:
        if row [0] == row[1] and row[0] == row[2]:
            return True
    for i in range(0, 2):
        if board[0][i] == board[1][i] and board[0] ==board[2][i] =
            return True
