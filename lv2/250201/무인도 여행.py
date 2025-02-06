# 딱 봤을 때, bfs 문제인데 bfs로 어떻게 풀었는지 기억이 안 남
# 돌면서 숫자를 발견하면 상하좌우로 이동해보며 값 계산
# 방문 후에는 X로 변경할 것

# google
from collections import deque


def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * M for _ in range(N)] # false로 초기화

    def bfs(x, y):
        visited[x][y] = True # 현재 위치 방문으로 변경
        queue = deque()
        queue.append((x, y))
        days = int(maps[x][y])
        while queue:
            x, y = queue.popleft() # 큐에서 뺌
            for i in range(4): # 4방향
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maps[nx][ny] != 'X':
                    queue.append((nx, ny))
                    days += int(maps[nx][ny])
                    visited[nx][ny] = True
        return days

    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]: # X이고 아직 방문하지 않은 경우 bfs 호출
                answer.append(bfs(i, j))
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)