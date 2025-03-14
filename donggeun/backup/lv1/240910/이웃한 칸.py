def solution(board, h, w):
    answer = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    current_color = board[h][w]
    for i in range(len(dx)):
        nx = h + dx[i]
        ny = w + dy[i]
        if(0 <= nx < len(board) and 0 <= ny < len(board)): # 배열 범위 넘어가는 인덱스는 조회하지 않도록 조건 부여
            if board[nx][ny] == current_color:
                answer += 1
    return answer

## main ##
board= [["blue", "red", "orange", "red"],
        ["red", "red", "blue", "orange"],
        ["blue", "orange", "red", "red"],
        ["orange", "orange", "red", "blue"]]
h= 1
w= 1
print(solution(board, h ,w))