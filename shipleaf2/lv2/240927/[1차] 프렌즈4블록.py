def solution(m, n, board):
    answer = 0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                if board[i][j] == board[i+1][j] == board[i+1][j+1]:
                    
    return answer