# gpt
from collections import deque

def solution(maps):
    # 2차원 배열로 변환
    n, m = len(maps), len(maps[0])
    maps = [list(row) for row in maps]  # 문자열을 리스트로 변환

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # 방문 체크 위함
    visited = [[False] * m for _ in range(n)]

    # 무인도에서 얻을 수 있는 총 식량을 저장할 리스트
    island_food = []

    # BFS
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True # 방문 표시
        total_food = int(maps[start_x][start_y])  # 현재 위치의 숫자를 식량으로 계산

        while queue:
            x, y = queue.popleft()

            # 4방향 탐색
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    total_food += int(maps[nx][ny])  # 숫자 더하기
                    queue.append((nx, ny))

        return total_food

    # 위치 탐색
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:  # 무인도(숫자가 있는 땅) & 방문 안한 곳
                island_food.append(bfs(i, j))

    if island_food:
        return sorted(island_food)  # 무인도가 존재하면 정렬 후 반환
    else:
        return [-1]  # 무인도가 하나도 없으면 -1 반환