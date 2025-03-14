def solution(n, t, m, p):
    answer = ''
    a = int_to_N((m*t), n)
    for i in range(len(a)):
        if (p + m*i) <= len(a):
            answer += a[p + m*i]
        else:
            break
    return answer

def int_to_N(mt, n):
    answer = '01'
    int = 1
    while True:
        int += 1
        b = int
        while b > 0:    
            remain = 0
            b = b // n
            remain = b % n
            if len(answer) < mt:
                answer = answer + str(remain)
            else:
                break
        if len(answer) >= mt:
            break
    print(answer)
    return answer

print(solution(2,4,2,1))