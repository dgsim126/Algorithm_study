def solution(n):
    answer = 0

    for i in range(1, n+1):
        sumnum = 0
        seq = i
        
        while seq <= n:
            sumnum += seq

            if sumnum == n:
                answer += 1 
                break
            elif sumnum > n:
                break

            seq += 1

    return answer