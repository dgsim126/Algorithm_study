from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 테스트
N, M = 7, 7
board = [
    list("#######"),
    list("#...RB#"),
    list("#.#####"),
    list("#.....#"),
    list("#####.#"),
    list("#O....#"),
    list("#######")
]

rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j # 빨간 구슬 좌표 저장
        elif board[i][j] == 'B':
            bx, by = i, j # 파란 구슬 좌표 저장

def bfs():
    queue = deque([(rx, ry, bx, by, 0)])  # (빨간 구슬 x, y, 파란 구슬 x, y, 이동 횟수)
    visited = set()
    visited.add((rx, ry, bx, by))

    while queue:
        r_x, r_y, b_x, b_y, depth = queue.popleft()

        # 10번 이상이면 실패
        if depth >= 10:
            return -1

        for dx, dy in directions: # 구슬 기울이며 탐색
            # 빨간 구슬 이동
            nr_x, nr_y = r_x, r_y
            while board[nr_x + dx][nr_y + dy] != '#' and board[nr_x][nr_y] != 'O':
                nr_x += dx
                nr_y += dy

            # 파란 구슬 이동
            nb_x, nb_y = b_x, b_y
            while board[nb_x + dx][nb_y + dy] != '#' and board[nb_x][nb_y] != 'O':
                nb_x += dx
                nb_y += dy

            # 파란 구슬이 구멍에 빠진 경우
            if board[nb_x][nb_y] == 'O':
                continue

            # 빨간 구슬이 구멍에 빠진 경우 (성공)
            if board[nr_x][nr_y] == 'O':
                return depth + 1

            # 두 구슬이 같은 칸에 도착한 경우 -> 먼 거리를 이동한 구슬을 한 칸 뒤로 (늦게 도착했을 것이므로)
            if nr_x == nb_x and nr_y == nb_y:
                if abs(nr_x - r_x) + abs(nr_y - r_y) > abs(nb_x - b_x) + abs(nb_y - b_y):
                    nr_x -= dx
                    nr_y -= dy
                else:
                    nb_x -= dx
                    nb_y -= dy

            # 방문 여부 체크, 방문 아직이면 큐에 삽입
            if (nr_x, nr_y, nb_x, nb_y) not in visited:
                visited.add((nr_x, nr_y, nb_x, nb_y))
                queue.append((nr_x, nr_y, nb_x, nb_y, depth + 1))

    return -1

print(bfs())