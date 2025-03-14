def solution(nums):
    half= len(nums)//2
    nums= len(set(nums))

    if(half < nums):
        return half
    else:
        return nums


## main ##
nums= [3,3,3,2,2,2]
print(solution(nums))