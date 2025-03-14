def solution(board, h, w):
    answer = 0
    n = len(board) - 1
    if h == 0 and w == 0:
        arr = [board[h][w+1], board[h+1][w]]
    elif h == 0 and w == n:
        arr = [board[h][w-1], board[h+1][w]]
    elif h == n and w == 0:
        arr = [board[h-1][w], board[h][w+1]]
    elif h == n and w == n:
        arr = [board[h-1][w], board[h][w-1]]
    elif h == 0 and w > 0 and w < n:
        arr = [board[h][w-1], board[h][w+1], board[h+1][w]]
    elif h == n and w > 0 and w < n:
        arr = [board[h][w-1], board[h][w+1], board[h-1][w]]
    else:
        arr = [board[h-1][w],board[h+1][w],board[h][w+1],board[h][w-1]]
    for i in arr:
        if i == board[h][w]:
            answer += 1
    return answer