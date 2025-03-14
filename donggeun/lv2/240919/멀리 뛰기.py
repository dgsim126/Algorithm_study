# n의 변화는 피보나치 수열, 즉 dp를 활용

def solution(n):
    # 탈출조건
    if (n == 1):
        return 1
    elif (n == 2):
        return 2

    # 기본값
    dp= [0]*n
    dp[0]= 1
    dp[1]= 2

    for i in range(3, n+1):
        i-=1
        dp[i]= (dp[i-1]+dp[i-2])%1234567

    return dp[n-1]

## main ##
n= 5

for i in range(1, 10):
    print(solution(i))