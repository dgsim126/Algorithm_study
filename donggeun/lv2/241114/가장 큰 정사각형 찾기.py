def solution(board):
    # DP 테이블 초기화
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    max_side = 0

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                # 첫 행, 첫 열이 아니면 DP 계산
                if(i > 0 and j > 0):
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j]=1
                max_side = max(max_side, dp[i][j])  # 갱신

    return max_side * max_side


# 테스트
board1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board2 = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(solution(board1))  # 출력: 9
print(solution(board2))  # 출력: 4

