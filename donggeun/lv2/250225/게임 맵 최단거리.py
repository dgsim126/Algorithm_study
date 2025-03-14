from collections import deque


def solution(maps):

    n = len(maps)
    m = len(maps[0])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return maps[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return -1