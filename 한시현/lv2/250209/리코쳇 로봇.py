def solution(board):
    n, m = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    start, goal = None, None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)

    queue = [(start[0], start[1], 0)] # (x, y, 총 이동 횟수), 시작 지점 저장 후 start
    visited = set() # gpt : 방문 위치 기록, 중복 탐색 방지
    visited.add(start)

    while queue:
        x, y, moves = queue.pop(0)

        if (x,y) == goal:
            return moves

        for dx, dy in directions: # 4번 반복
            nx, ny = x, y # 4방향 탐색을 위해 초기 x,y 값 유지

            # gpt : 벽이나 장애물에 부딪힐 때까지 미끄러지듯 이동
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx = nx + dx
                ny = ny + dy

            # gpt : queue, visited 에 좌표 저장
            if (nx, ny) not in visited:
                queue.append((nx, ny, moves + 1))
                visited.add((nx, ny))

    return -1