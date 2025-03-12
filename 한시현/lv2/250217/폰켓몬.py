def solution(nums):
    n = len(nums) / 2  # 가져갈 수 있는 마릿수
    n_not = len(set(nums))  # 중복 없는 총 마릿수

    if n > n_not:
        return n_not
    else:
        return n