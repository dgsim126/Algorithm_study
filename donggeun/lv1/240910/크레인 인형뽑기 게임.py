def solution(board, moves):
    move= [moves[i]-1 for i in range(len(moves))]
    stack= [-100, -200]
    cnt= 0

    for point in move:
        for i in range(len(board[1])):
            if(board[i][point]!=0):
                stack.append(board[i][point])
                if(stack[-1]==stack[-2]):
                    stack.pop()
                    stack.pop()
                    cnt+=2
                board[i][point]= 0
                break

    return cnt

## main ##
board= [[0,0,0,0,0],
        [0,0,1,0,3],
        [0,2,5,0,1],
        [4,2,4,4,2],
        [3,5,1,3,1]]

moves= [1,5,3,5,1,2,1,4]
print(solution(board, moves))