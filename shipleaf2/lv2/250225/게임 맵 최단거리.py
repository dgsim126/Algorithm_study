from collections import deque

def solution(maps):
    row, col = len(maps), len(maps[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * col for _ in range(row)]
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, distance = queue.popleft()
        if x == row - 1 and y == col - 1:
            return distance

        for dx, dy in direction:
            rx, ry = x + dx, y + dy
            if 0 <= rx < row and 0 <= ry < col and not visited[rx][ry] and maps[rx][ry] == 1:
                visited[rx][ry] = True
                queue.append((rx, ry, distance + 1))

    return -1



print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))