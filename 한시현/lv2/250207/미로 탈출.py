# gpt
# 출발지(S) -> 레버(L) -> 출구(E) 최단시간
def solution(maps):
    n, m = len(maps), len(maps[0])  # 미로 크기
    start, lever, exit = None, None, None  # Nonetype : 값을 지정하지 않은 변수의 초기값

    # 미로에서 S, L, E 위치 탐색, 기록
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS 함수 (일반 리스트 사용)
    def bfs(start_pos, target_pos):
        queue = [(start_pos[0], start_pos[1], 0)]  # (x좌표, y좌표, 이동거리)

        visited = [[False] * m for _ in range(n)] # 방문 처리를 위해 2차원 리스트 False로 초기화
        visited[start_pos[0]][start_pos[1]] = True  # 시작점 방문 처리

        while queue:
            x, y, steps = queue[0]  # 큐의 첫 번째 요소 가져오기
            queue.pop(0)  # 첫 번째 요소 제거 (리스트의 pop(0) 사용)

            # 목표 위치 도달 시 최단 거리 반환
            if (x, y) == target_pos:
                return steps

            # 4방향 탐색
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                # 범위 체크 & 벽이 아니고 & 방문하지 않은 곳이면 이동
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))  # 이동거리 +1

        return -1  # 목표 지점에 도달할 수 없는 경우

    # `S -> L` 거리 찾기
    to_lever = bfs(start, lever)
    if to_lever == -1:  # 레버까지 못 가면 탈출 불가
        return -1

    # `L -> E` 거리 찾기
    to_exit = bfs(lever, exit)
    if to_exit == -1:  # 출구까지 못 가면 탈출 불가
        return -1

    return to_lever + to_exit  # 총 이동 거리 반환