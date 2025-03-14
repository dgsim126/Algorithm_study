# gpt
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # BFS를 위한 리스트 큐 생성 (시작점은 (0, 0))
    queue = [(0, 0)]
    
    # BFS 시작
    while queue:
        x, y = queue.pop(0)  # 리스트의 첫 번째 요소를 꺼냄
        
        # 현재 위치에서 상하좌우로 이동
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy

            # 맵의 범위를 벗어나지 않고, 이동 가능한 곳(1)일 때만 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이전 위치에서 1을 더해서 이동 거리 갱신
                maps[nx][ny] = maps[x][y] + 1
                # 큐에 다음 위치를 추가
                queue.append((nx, ny))
    
    # 도착 지점에 도달하지 못하면 -1 반환
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]  # 도착 지점의 값이 최단 경로 길이
