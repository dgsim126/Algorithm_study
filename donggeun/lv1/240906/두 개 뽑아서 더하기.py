def solution(num):
    global answer
    answer= []

    dfs(0, 0, [], num) # depth, start, result, num

    return sorted(list(set(answer)))

def dfs(depth, start, result, lst):
    global answer
    if(depth==2):
        # print(result)
        answer.append(sum(result))
        return
    else:
        for i in range(start, len(lst)):
            result.append(lst[i])

            dfs(depth+1, i+1, result, lst)

            result.pop()


## main ##
numbers = [-2, 2, 3, -3]
print(solution(numbers))