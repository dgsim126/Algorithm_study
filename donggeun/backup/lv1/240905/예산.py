def solution(d, budget):
    answer = 0
    d= sorted(d)

    for i in range(len(d)):
        answer+= d[i]
        if(answer>budget):
            return i

    return len(d)

## main ##
d= [1,3,2,5,4]
budget= 9
print(solution(d, budget))