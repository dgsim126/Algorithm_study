# GPT

from collections import deque

def solution(maps):
    # 방향벡터 (동, 서, 남, 북)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = len(maps)   # 세로
    m = len(maps[0])    # 가로

    # BFS 큐 초기화
    queue = deque([(0, 0)]) # 시작점 추가
    visited = [[-1] * m for _ in range(n)]  # 방문 체크 및 거리를 기록하는 배열, -1로 초기화
    visited[0][0] = 1  # 시작점은 1로 설정

    # BFS 시작
    while queue:    # queue가 비어 있지 않은 동안은 계속 실행
        x, y = queue.popleft()  # 현재 위치 꺼내기

        # 상대팀 진영 도착 확인
        if x == n-1 and y == m-1:   # 상대팀 진영 좌표 도착
            return visited[x][y]    

        # 네 방향으로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위를 벗어나지 않고, 이동할 수 있는 칸일 때
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1: # 맵 범위 안 + 벽이 아닌곳이면 
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # 상대 팀 진영에 도착할 수 없을 때
    return -1

# 테스트
maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

# 결과 출력
print(solution(maps))
