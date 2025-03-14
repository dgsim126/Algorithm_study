from itertools import combinations

def solution(nums):
    answer = int(len(nums)*(len(nums)-1)*(len(nums)-2)/6)
    for comb in combinations(nums, 3):
        for i in range(2,int(sum(comb)/2)+1):
            if sum(comb)%i == 0:
                answer -= 1
                break
            
    return answer

print(solution([1,2,3,4]))