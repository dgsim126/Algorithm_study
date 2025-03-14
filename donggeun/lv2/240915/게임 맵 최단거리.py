def solution(maps):
    global result
    result = []
    current_x = 0
    current_y = 0
    destination_x = len(maps) - 1
    destination_y = len(maps[0]) - 1
    is_arrived = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]

    # 시작 지점 방문 처리
    is_arrived[current_x][current_y] = 1

    # DFS 시작 (depth 1)
    dfs(1, current_x, current_y, destination_x, destination_y, maps, is_arrived)

    # 도착하지 못한 경우 처리
    if len(result) == 0:
        return -1
    else:
        return min(result)

def dfs(depth, current_x, current_y, destination_x, destination_y, maps, is_arrived):
    global result
    x = [-1, 0, 1, 0]  # 북 동 남 서
    y = [0, 1, 0, -1]  # 북 동 남 서

    # 탈출 조건: 목적지에 도착하면 depth 저장
    if current_x == destination_x and current_y == destination_y:
        result.append(depth)
        return

    # 네 방향으로 이동
    for i in range(4):
        next_x = current_x + x[i]
        next_y = current_y + y[i]

        # 맵 범위 내에 있고, 벽이 아니며, 방문하지 않은 곳일 때만 이동
        if (0 <= next_x < len(maps) and 0 <= next_y < len(maps[0])  #### 수정 됨 ###
                and maps[next_x][next_y] == 1 and is_arrived[next_x][next_y] == 0):

            # 방문 처리
            is_arrived[next_x][next_y] = 1

            # DFS
            dfs(depth + 1, next_x, next_y, destination_x, destination_y, maps, is_arrived)  #### 수정 됨 ###

            # 백트래킹
            is_arrived[next_x][next_y] = 0

## main ##
maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

maps2 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 0],
         [0, 0, 0, 0, 1]]

print(solution(maps))
print(solution(maps2))
