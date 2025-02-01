def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        visited[x][y] = True
        total_food = int(maps[x][y])

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                total_food += dfs(nx, ny)
        
        return total_food
    
    local_food = []

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != "X" and not visited[i][j]:
                local_food.append(dfs(i, j))

    return sorted(local_food) if local_food else [-1]

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))


from collections import deque

def solution(maps):
    rows, cols = len(maps), len(maps[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        total_food = 0
        
        while queue:
            cx, cy = queue.popleft()
            total_food += int(maps[cx][cy])  # 현재 위치의 식량 추가

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        return total_food

    local_food = []

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] != "X" and not visited[i][j]:
                local_food.append(bfs(i, j))

    return sorted(local_food) if local_food else [-1]