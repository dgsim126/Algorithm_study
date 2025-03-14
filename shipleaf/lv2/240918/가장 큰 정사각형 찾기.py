# GPT

def solution(board):
    # board 가로, 세로 길이
    n = len(board)  # 세로
    m = len(board[0])   # 가로
    
    # dp 테이블 초기화
    dp = [[0] * m for _ in range(n)]
    
    # 최대 변의 길이를 저장할 변수
    max_side = 0
    
    # 첫 번째 행과 첫 번째 열은 원래 값을 그대로 사용
    for i in range(n):
        dp[i][0] = board[i][0]
        max_side = max(max_side, dp[i][0])
    
    for j in range(m):
        dp[0][j] = board[0][j]
        max_side = max(max_side, dp[0][j])
    
    # 나머지 칸에 대해 DP 값을 채워넣음
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                # 위쪽, 왼쪽, 대각선 왼쪽 위의 값 중 최솟값을 사용
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    # 최대 변의 길이를 제곱해서 넓이를 반환
    return max_side ** 2
