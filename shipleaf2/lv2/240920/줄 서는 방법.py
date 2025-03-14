import math     # math 기억이 안났음..

def solution(n, k):
    answer = []
    num_list = []
    for i in range(1,n+1):
        num_list.append(i)
    while n > 0:
        index = math.ceil(k/factorial(n-1)) - 1
        k = k - (factorial(n-1) * index)
        answer.append(num_list[index])
        num_list.pop(index)
        n = n - 1
    return answer


def factorial(n):
    number = 1
    for i in range(1,n+1):
        number = number * i
    return number

print(solution(3,5))