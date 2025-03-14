def solution(n):
    answer = int(reverse_ternary(int_to_ternary(n)), 3)
    return answer

def int_to_ternary(n):
    ternary=''
    while n != 0:
        remain = n%3
        ternary = str(remain) + ternary
        n = n//3
    return ternary

def reverse_ternary(ternary):
    return ternary[::-1]

# print(reverse_ternary(int_to_ternary(45)))

# a = '김선엽'

# print(a[::-1])

