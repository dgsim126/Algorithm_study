from itertools import combinations

def solution(nums):
    answer = 0
    allnum = []
    allcom = list(combinations(nums, 3))

    for com in allcom:
        allnum.append(sum(com))

    for num in allnum:
        check = []
        for i in range(2, num):
            check.append(i)

        isit = True
        for i in check:
            if num % i == 0:
                isit = False
                break
        if isit:
            answer += 1

    return answer