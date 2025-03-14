def solution(n, l, r):
    answer = 0
    for i in range(l, r+1):
        index = i // 5**(n-1)
        if i % 5 == 3:
            continue
        else:
            if i / (5**(n-1)) > 2 and i / (5**(n-1)) <= 3:
                continue
            else:
                if (i - index*(5**(n-1))) >= 51 and (i - index*(5**(n-1))) <= 75:
                    continue
                elif (i - index*(5**(n-1))) / 5 > 2 and (i - index*(5**(n-1))) / 5 <= 3:
                    continue
                else:
                    answer += 1
        
    return answer

print(solution(2,4,17))