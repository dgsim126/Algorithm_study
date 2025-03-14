def solution(board, moves):
    answer = 0
    n = len(board)
    dic = {}
    arr = []
    for i in range(n):
        dic[i+1] = []
    for i in range(n,0,-1):
        for j in range(n):
            if board[i-1][j] != 0:
                dic[j+1].append(board[i-1][j])
    m = 0
    for i in range(len(moves)):
        if dic[moves[i]] != []:
            arr.append(dic[moves[i]].pop())
            m+=1
            print(arr)
            break
        else:
            m+=1
            continue
    
    for move in moves:
        if dic[move]:
            arr.append(dic[move].pop())
            print(arr)

            if len(arr) >= 2 and arr[-1] == arr[-2]:
                arr.pop()
                arr.pop()
                answer += 2
    
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))    # 4, 3, 1, 1, 3, 2, 1, 3
print(solution([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],[1,2,3,4,5]))
print(solution([[0, 0, 0, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0],[0, 0, 1, 0, 0]], [3,3,3,3]))

