def solution(n):
    answer = 0
    base3 = []

    while n>0:
        base3.append(n % 3)
        n = n//3
    base3.reverse()

    for i in range(len(base3)):
        answer += base3[i] * (3**i)
        
    return answer