# gpt
def solution(n):
    number = 1
    total_num = n*(n+1) // 2
    triangle = [[0]*(i+1) for i in range(n)]

    x,y = 0,0
    moves = [[1, 0], [0, 1], [-1, -1]]
    current_move = 0

    for _ in range(total_num):
        triangle[x][y] = number

        # 다음 위치 계산
        nx, ny = x + moves[current_move][0], y + moves[current_move][1]

        # 경계 조건 확인, 방향 전환
        # 삼각형의 위로 벗어났을 때, 아래로 벗어났을 때, 대각선 범위 벗어났을 때(열보다 행이 커졌을때), 삼각형 다 채워졌을 때
        if nx < 0 or ny < 0 or nx >= n or ny > nx or triangle[nx][ny] != 0:
            current_move = (current_move + 1) % 3  # 방향 전환
            nx, ny = x + moves[current_move][0], y + moves[current_move][1]

        x, y = nx, ny
        number += 1

        result = []
        for i in range(len(triangle)):
            result += triangle[i]

    return result