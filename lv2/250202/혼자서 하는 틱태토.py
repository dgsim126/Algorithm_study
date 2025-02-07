def solution(board):
    num_o = 0
    num_x = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "O":
                num_o += 1
            elif board[i][j] == "X":
                num_x += 1
    if (num_o - num_x) > 1 or (num_o - num_x) < 0:
        return 0
    
    def check_winner(symbol):
        for i in range(3):
            if all(board[i][j] == symbol for j in range(3)):
                return True
            if all(board[j][i] == symbol for j in range(3)):
                return True
            
        if all(board[i][i] == symbol for i in range(3)):
            return True
        if all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    O_wins = check_winner('O')
    X_wins = check_winner('X')

    if O_wins and X_wins:
        return 0

    if O_wins and num_o != num_x + 1:
        return 0

    if X_wins and num_o != num_x:
        return 0

    return 1

print(solution(["OOO", "XOX", "XXO"]))
