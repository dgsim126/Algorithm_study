# GPT 사용

# def solution(number):
#     answer = 0
#     num_zero = 0
#     max = max(number)
#     if max(number)>1:
#         count = 0
#         i = 0
#         while count < 2 and i < len(number):
#             if number[i] != max:
#                 if max 
#     return answer

## 다 따로 해보자

# def solution1(number):
#     number.sort()
#     sum = 0
#     count = 0
#     n = 0
#     if number[0] == 0:
#         return 0
#     elif number[0] > 0:
#         return 0
#     elif number[-1] < 0:
#         return 0
    
#     for i in range(len(number)):
#         if number[i] >= 0:
#             n = i
    
#     for i in range(n):
#         sum += number[i]
#         count += 1
#         for j in range(n, len(number)):

        
# def solution(number):
#     answer = 0
#     return answer

from itertools import combinations

def solution(number):
    count = 0
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            count += 1
    return count
