# 테스트 케이스 13개 중 2개 실패(정확성 84.6)
# gpt를 사용하여 반례 확인 -> 중복된 조합이 사용되고 있음 e.g. [-1. -1, 2, 2]

def solution(lst):
    global cnt
    cnt = 0
    is_used= [False]*len(lst)
    result= [None]*3

    dfs(0, is_used, result, lst)

    return cnt

def dfs(depth, is_used, result, lst):
    global cnt
    if(depth==3):
        if(sum(result)==0):
            print(result, sum(result))
            cnt+= 1
        return
    else:
        for i in range(len(lst)):
            if((is_used[i]==False) and (depth == 0 or result[depth - 1] <= lst[i])):
                is_used[i]= True
                result[depth]= lst[i]
                dfs(depth+1, is_used, result, lst)
                is_used[i]= False


## main ##
lst= [-3, -2, -1, 0, 1, 2, 3]
global total
print(solution(lst))