# 테스트 케이스 하나 실패 => n = 1일때의 상황 고려

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    if n >= 2:
        dp[2] = 2   # n = 1 일때 코드 추가
    
    if n > 2:
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

    answer = dp[n] % 1234567
    return answer