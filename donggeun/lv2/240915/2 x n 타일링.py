# 시간초과
import math

def solution(n):
    result= 0
    # 현재 주어진 값일 때 가능한 모든 경우 계산
    # 현재 값에서 -2를 한 후 해당 값이 0보다 크거나 같다면 가능한 모든 경우 계산

    for i in range(n, -1, -2):
        # 현재 i가 세로로 긴 직사각형의 개수를 의미
        # x= n-i라고 한다면 x는 가로로 긴 직사각형의 개수
        # x//2를 하면 해당 공간 범위를 나타낼 수 있음
        # i+(x//2) C i가 내가 구하고자 하는 값!
        x= (n-i)//2
        result+=(C(i+x, i))
        # print(f"{i+x}C{i}= {C(i+x, i)}")
        result %= 1000000007

    return result

def C(n, i):
    return math.factorial(n) // (math.factorial(i) * math.factorial(n - i))

## main ##
print(solution(30))
