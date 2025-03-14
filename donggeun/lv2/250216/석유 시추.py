
from collections import deque

def solution(land):
    n, m = len(land), len(land[0])  # 세로(n), 가로(m)
    oil_map = [[0] * m for _ in range(n)]  # 각 칸이 속한 석유 덩어리 ID 저장
    oil_sizes = {}  # 각 석유 덩어리 ID별 크기 저장

    dx = [0, 0, 1, -1]  # 동, 서, 남, 북
    dy = [1, -1, 0, 0]

    def bfs(y, x, oil_id):
        """BFS를 사용하여 석유 덩어리를 탐색하고 크기를 반환"""
        queue = deque([(y, x)])
        oil_map[y][x] = oil_id
        size = 1

        while queue:
            cy, cx = queue.popleft()
            for i in range(4):
                ny, nx = cy + dy[i], cx + dx[i]
                if 0 <= ny < n and 0 <= nx < m and land[ny][nx] == 1 and oil_map[ny][nx] == 0:
                    oil_map[ny][nx] = oil_id
                    size += 1
                    queue.append((ny, nx))

        return size

    # Step 1: BFS로 석유 덩어리 찾기 (한 번만 탐색)
    oil_id = 1  # 석유 덩어리 ID (0은 미방문 상태)
    for y in range(n):
        for x in range(m):
            if land[y][x] == 1 and oil_map[y][x] == 0:
                oil_sizes[oil_id] = bfs(y, x, oil_id)
                oil_id += 1

    # Step 2: 각 열에서 최대로 뽑을 수 있는 석유량 계산
    max_oil = 0
    for x in range(m):  # 열을 순회하며 석유량 계산
        seen_oil = set()  # 해당 열에서 만난 석유 덩어리 ID 저장
        for y in range(n):
            if oil_map[y][x] > 0:
                seen_oil.add(oil_map[y][x])
        total_oil = sum(oil_sizes[oil] for oil in seen_oil)  # 중복된 석유 덩어리 크기는 한 번만 합산
        max_oil = max(max_oil, total_oil)

    return max_oil
