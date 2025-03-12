def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    answer = 45 - sum
    
    return answer