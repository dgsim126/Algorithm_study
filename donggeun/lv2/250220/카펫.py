# yellow를 만들 수 있는 side, up를 구하고, 해당되는 brown의 개수를 구하면 된다

def solution(brown, yellow):
    # n*m이 yellow가 되는 n,m을 모두 찾아보자!
    last_n = -1
    for n in range(1, yellow + 1):
        if (yellow % n == 0):
            m = int(yellow / n)
            if (last_n == m):
                return
            last_n = n
            print(n, m)

            temp = m * 2 + n * 2 + 4
            if (temp == brown):
                # print("!!!!!!!!!!!!!", m+2, n+2)
                return [m + 2, n + 2]