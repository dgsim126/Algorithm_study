# GPT

def solution(n):
    MOD = 1000000007
    
    if n % 2 != 0:  # 홀수
        return 0
    
    # dp 테이블
    dp = [0] * (n + 1)
    
    # 기본적인 경우의 수
    dp[0] = 1  # 아무 타일도 사용하지 않는 경우
    dp[2] = 3  # 가로 길이가 2일 때는 3가지
    
    # DP 테이블을 채웁니다.
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i - 2] * 3) % MOD
        
        # 이전의 모든 패턴을 더해줍니다.
        for j in range(4, i + 1, 2):
            dp[i] = (dp[i] + dp[i - j] * 2) % MOD

    return dp[n]

# 테스트
n = 6
print(solution(n))
