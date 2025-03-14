# gpt's help

def solution(board):
    # DP 테이블 초기화 (board와 동일 크기)
    dp = [[0] * len(board[0]) for _ in range(len(board))]

    max_side = 0  # 가장 큰 정사각형의 한 변의 길이 저장

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                # 첫 행, 첫 열이 아니면 DP 계산
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 1
                max_side = max(max_side, dp[i][j])  # 최대 정사각형 변 갱신

            # DP 테이블의 현재 상태 출력
            print(f"DP 테이블 상태 (i={i}, j={j}):")
            for row in dp:
                print(row)
            print()

    # 가장 큰 정사각형의 넓이 반환
    print(f"최대 변의 길이: {max_side}")
    return max_side * max_side


# 테스트
board1 = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
board2 = [[0, 0, 1, 1], [1, 1, 1, 1]]
print(f"최종 넓이: {solution(board1)}")  # 출력: 9
print(f"최종 넓이: {solution(board2)}")  # 출력: 4
