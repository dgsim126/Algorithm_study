def solution(n,a,b):
    c = 0
    d = n
    while d != 1:
        d = d / 2
        c += 1
    while n > 2:
        if (a <= n/2 and b > n/2) or (a > n/2 and b <= n/2):
            return c
        else:
            if a > n/2:
                a = a - n/2
                b = b - n/2
                n = n/2
                c -= 1
            else:
                n = n/2
                c -= 1
    return 1

print(solution(8,4,7))