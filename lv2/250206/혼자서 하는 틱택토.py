# 1. 승자가 두 명인 경우 0
# 2. o, x의 개수 차이가 2개 이상 0
# 3. x의 개수가 하나 더 많음
#

def solution(board):
    # 2번 확인
    cnt_O= 0
    cnt_X= 0
    for i in range(3):
        for j in range(3):
            if(board[i][j]=="O"):
                cnt_O+=1
            elif(board[i][j]=="X"):
                cnt_X+=1

    if(abs(cnt_O-cnt_X)>=2):
        return 0

    # 3번 확인
    if(cnt_X>cnt_O):
        return 0

    # 1번 확인
    lst= [[[0,0], [0,1], [0,2]], # 가로
          [[1,0], [1,1], [1,2]],
          [[2,0], [2,1], [2,2]],
          [[0,0], [1,0], [2,0]], # 세로
          [[0,1], [1,1], [2,1]],
          [[0,2], [1,2], [2,2]],
          [[0,0], [1,1], [2,2]], # 대각선
          [[0,2], [1,1], [2,0]]]
    win_O = 0
    win_X = 0
    print(lst[0][1][1])

    for i in range(8):
        if(board[lst[i][0][0]][lst[i][0][1]]==board[lst[i][1][0]][lst[i][1][1]]==board[lst[i][2][0]][lst[i][2][1]]):
            if(board[lst[i][0][0]][lst[i][0][1]]=="X"):
                win_X+=1
            elif(board[lst[i][0][0]][lst[i][0][1]]=="O"):
                win_O+=1
    # 1번 확인
    if(win_O>=1 and win_X>=1):
        return 0

    # O가 승리한 경우 - gpt
    if win_O and cnt_O != cnt_X + 1:
        return 0

    # X가 승리한 경우 - gpt
    if win_X and cnt_O != cnt_X:
        return 0

    return 1




## main ##
board= ["OOO", "...", "XXX"]
print(solution(board))