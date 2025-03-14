# from itertools import combinations

# def solution(nums):
#     answer = 0
#     n = len(nums)//2
#     for comb in combinations(nums, n):
#         if len(list(set(comb))) > answer:
#             print(len(list(set(comb))))
#             answer = len(list(set(comb)))
#     return answer

def solution(nums):
    answer = 0
    num_pokemon = len(nums)/2
    n = len(list(set(nums)))
    if num_pokemon >= n:
        answer = n
    else:
        answer = num_pokemon
    return answer

# 테스트
# print(set([1,2,3,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
print(solution([3, 1, 2, 3]))
