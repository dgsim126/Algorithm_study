def solution(nums):
    how= len(set(nums))
    print("종류: ", how)
    if(how < len(nums)/2):
        return how
    else:
        return len(nums)/2

## main ##
nums= [3,1,2,3]
print(solution(nums))