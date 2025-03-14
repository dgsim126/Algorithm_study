def solution(n):    
    answer = 0
    if n % 2 == 0:  # n이 짝수일때
        case = n // 2   # n을 2로 나누었을때 2블럭이 가로로 채워지는 케이스 수가 나옴
        answer = 1 + find_case(case, n) # 1은 모두가 2블럭일때를 더해준것
    if n % 2 == 1:  # n이 홀수일때
        case = (n-1) // 2
        answer = case + 1 + find_case(case, n)
    return int(answer)

def find_case(case, n):
    total = 1
    for i in range(1, case):
        total += (factorial(n-(2*i)+i)/(factorial(i) * factorial(n-(2*i))))
    return total

def factorial(number):
    factorial_sum = 1
    for i in range(number, 0, -1):
        factorial_sum = factorial_sum * i
    return factorial_sum

print(solution(4))