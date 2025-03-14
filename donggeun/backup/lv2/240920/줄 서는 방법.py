# 전형적인 dfs 문제(시간초과, 효율성 실패)

def solution(n, k):
    global cnt, answer, found
    found= False
    cnt= 0
    answer= []
    is_used = [False]*n
    result = [0]*n

    dfs(0, is_used, result, n, k)
    return answer  # 원하는 result를 찾았을 때 answer에 저장

def dfs(depth, is_used, result, n, k):
    global cnt, answer, found

    if(found==True):
        return

    # 탈출조건
    if(depth==n):
        cnt += 1
        if(cnt==k):
            answer= result[:]
            found= True
        return

    for i in range(n):
        if(is_used[i]==False):
            is_used[i]= True
            result[depth]= i+1

            dfs(depth+1, is_used, result, n, k)

            is_used[i]= False

# main
n = 3
k = 5
print(solution(n, k))
