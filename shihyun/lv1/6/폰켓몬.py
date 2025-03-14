def solution(nums):
    answer = 0
    n = len(nums) / 2 # 가져갈 수 있는 마릿수
    nofnotd = len(list(set(nums))) # 중복 없는 총 마릿수
    
    if n > nofnotd:
        return nofnotd
    else:
        return n