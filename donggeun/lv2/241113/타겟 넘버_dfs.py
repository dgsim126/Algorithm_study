def dfs(numbers, current_sum, target, depth):
    global cnt
    # 탈출조건
    if(depth==len(numbers)):
        if(target==current_sum):
            cnt+=1
        return

    dfs(numbers, current_sum+numbers[depth], target, depth+1)
    dfs(numbers, current_sum-numbers[depth], target, depth+1)


def solution(numbers, target):
    global cnt
    cnt= 0

    dfs(numbers, 0, target, 0)
    return cnt



## main ##
numbers= [4, 1, 2, 1]
target= 4
print(solution(numbers, target))