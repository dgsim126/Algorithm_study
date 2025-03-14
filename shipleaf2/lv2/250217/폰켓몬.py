def solution(nums):
    pick_num = len(nums) / 2
    nums = set(nums)
    if len(nums) <= pick_num:
        return len(nums)
    else:
        return int(pick_num)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))