# gpt
def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1) # n칸까지 도달하는 방법의 수를 저장할 dp 배열
    dp[1] = 1 # 1칸에 도달하는 방법 1가지 (1칸)
    dp[2] = 2 # 2칸에 도달하는 방법 2가지 (1칸 + 1칸, 2칸)
    
    # 피보나치 수열
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567 # 메모리 오버플로우 방지

    return dp[n]