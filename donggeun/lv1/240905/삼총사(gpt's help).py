def solution(lst):
    global cnt
    cnt = 0

    dfs(0, 0, [], lst)

    return cnt

def dfs(depth, start, result, lst):
    global cnt
    if(depth==3):
        if(sum(result)==0):
            cnt+=1
        return
    else:
        for i in range(start, len(lst)):  # start 이후의 인덱스만 탐색
            dfs(depth+1, i+1, result+[lst[i]], lst)

## main ##
lst = [-3, -2, -1, 0, 1, 2, 3]
print(solution(lst))
