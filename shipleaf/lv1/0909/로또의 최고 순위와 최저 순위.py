def solution(lottos, win_nums):
    answer = []
    dic = {}
    numbers = lottos + win_nums
    dic[0] = 0
    for i in numbers:
        dic[i] = 0
    for i in lottos:
        dic[i] = dic[i] + 1
    count_zero = dic[0]
    count = 0
    for i in win_nums:
        if dic[i] == 1:
            count += 1
    
    min = count
    max = min + count_zero

    answer.append(score(max))
    answer.append(score(min))

    return answer

def score(n):
    if n == 6:
        return 1
    elif n == 5:
        return 2
    elif n == 4:
        return 3
    elif n == 3:
        return 4
    elif n == 2:
        return 5
    else:
        return 6

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))   # 0이 없는 경우도 고려