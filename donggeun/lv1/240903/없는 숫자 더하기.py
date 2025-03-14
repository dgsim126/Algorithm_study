def solution(numbers):
    answer = 0

    for i in range(len(numbers)):
        answer+= numbers[i]

    return 45-answer

## main ##
numbers= [1,2,3,4,6,7,8,0]
print(solution(numbers))