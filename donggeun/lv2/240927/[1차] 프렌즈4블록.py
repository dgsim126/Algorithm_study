# gpt's help
def solution(m, n, board):
    total_removed = 0

    # 문자열을 리스트로 변환하여 수정 가능하게 함
    board = [list(row) for row in board]

    while True:
        index = set()  # 각 루프마다 새로운 set을 생성

        # 사라지게 될 블록들 조회
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1] and board[i][j] != '0':
                    index.add((i, j))
                    index.add((i, j + 1))
                    index.add((i + 1, j))
                    index.add((i + 1, j + 1))

        # 블록이 더 이상 사라질 것이 없으면 종료
        if not index:
            break

        # 사라지게 될 블록들을 '0'으로 변경
        for i in index:
            board[i[0]][i[1]] = '0'

        # 지워진 블록 수 누적
        total_removed += len(index)

        # 열별로 블록 아래로 이동
        for col in range(n):
            empty_row = m - 1  # 가장 아래쪽부터 빈 공간을 채워나감
            for row in range(m - 1, -1, -1):
                if board[row][col] != '0':  # 블록이 있는 경우
                    board[empty_row][col] = board[row][col]
                    if empty_row != row:  # 빈 공간이 아닌 위치로 블록을 옮긴 경우
                        board[row][col] = '0'
                    empty_row -= 1  # 빈 공간 위치를 위로 이동

    # 최종 상태 출력
    for row in board:
        print(''.join(row))

    return total_removed

## main ##
m = 4
n = 5
board = ["CCBDE",
         "AAADE",
         "AAABF",
         "CCBBF"]
print(solution(m, n, board))
