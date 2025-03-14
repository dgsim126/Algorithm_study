## bfs의 개념을 잘 몰라서 gpt에게 풀어달라고 함
from collections import deque


def solution(maps):
    # 맵 크기
    n = len(maps)
    m = len(maps[0])

    # 방향 벡터 (북, 동, 남, 서)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # BFS에 사용할 큐
    queue = deque()
    # 시작점 (0, 0)을 큐에 넣고 시작
    queue.append((0, 0))

    # 방문 처리 배열은 따로 만들지 않고, maps를 이용해서 방문 처리 (1 -> 방문 가능, 0 -> 벽 또는 방문 완료)

    # BFS 시작
    while queue:
        x, y = queue.popleft()

        # 목적지에 도착하면 그 값을 반환
        if x == n - 1 and y == m - 1:
            return maps[x][y]

        # 현재 위치에서 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위 내에 있고, 벽이 아니며, 아직 방문하지 않은 곳일 때만 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이동할 수 있는 곳을 큐에 추가하고, 그 위치까지의 거리를 갱신
                maps[nx][ny] = maps[x][y] + 1  # 거리 갱신 (방문 처리도 포함됨)
                queue.append((nx, ny))

    # 큐가 끝날 때까지 목적지에 도착하지 못했다면 -1 반환
    return -1


# 테스트 케이스
maps1 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1]]

maps2 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1]]

print(solution(maps1))  # 11 반환 (valid path)
print(solution(maps2))  # -1 반환 (no valid path)
