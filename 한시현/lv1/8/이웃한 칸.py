def solution(board, h, w):
    n = len(board)
    count = 0
    if h+1 < n and board[h+1][w] == board[h][w]:
        count += 1
    if w+1 < n and board[h][w+1] == board[h][w]:
        count += 1
    if 0 <= h-1 and board[h-1][w] == board[h][w]:
        count += 1
    if 0 <= w-1 and board[h][w-1] == board[h][w]:
        count += 1

    return count
    
# def solution(board, h, w):
#     n = len(board)
#     count = 0
#     dh = [0,1,-1,0]
#     dw = [1,0,0,-1]
#     for i in range(4):
#         h_check = h + dh[i]
#         w_check = w + dw[i]
#         if 0 <= h_check < n and 0 <= w_check < n and board[h_check][w_check] == board[h][w]:
#             count += 1

#     return count