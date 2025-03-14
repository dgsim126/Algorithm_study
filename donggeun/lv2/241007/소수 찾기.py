# dfs로 모든 경우를 조회하고 리스트에 넣는다.
# 리스트의 있는 값들이 소수인지 확인.
# sqrt()까지 for문을 돌리며 나눠지지 않는다면 그것은 소수(전에 풀었던 문제)

def solution(numbers):
    global answer
    answer= []

    lst= list(numbers)
    is_used= [False]*len(lst)
    result= []

    for i in range(1, len(lst)+1):
        dfs(lst, is_used, result, 0, i)

    answer = list(map(int, [''.join(item) for item in answer]))

    return prime(answer)

def prime(lst):
    cnt= 0
    lst= set(lst)
    lst= list(lst)
    for num in lst:
        if(num==0 or num==1):
            continue
        flag= True
        for i in range(2, int(num**(1/2))+1, 1):
            if(num%i==0): # 소수가 아님
                flag= False
                break
        if(flag== True):
            cnt+=1

    return cnt




def dfs(lst, is_used, result, depth, max_):
    global answer
    if(depth>=max_):
        answer.append(result[:])
        return

    for i in range(len(lst)):
        if(is_used[i]==False):
            is_used[i]= True
            result.append(lst[i])
            # print(result)

            dfs(lst, is_used, result, depth+1, max_)

            is_used[i]= False
            result.pop()

## main ##
numbers= "17"
print(solution(numbers))
