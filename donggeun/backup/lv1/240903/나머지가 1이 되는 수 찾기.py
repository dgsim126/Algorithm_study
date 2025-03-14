def solution(n):
    answer = 0

    for i in range(1, n):
        if(n%i==1):
            return i

    return answer

## main ##
print(solution(10))
print(solution(12))