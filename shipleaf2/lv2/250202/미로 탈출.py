from collections import deque

def solution(maps):
    answer = 0

    def findStart(maps):
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == "S":
                    return i, j
                
    def BFSSToL(maps, x, y):
        loc = deque([(x, y)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        time = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while loc:
            lx, ly = loc.popleft()
            if maps[lx][ly] == "L":
                return lx, ly, time
            time += 1

            for dx, dy in direction:
                nx, ny = lx + dx, ly + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[lx][ly] != "X":
                    visited[nx][ny] = True
                    loc.append([nx, ny])

    def BFSLToE(x, y, time):
        loc = deque([(x, y)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        time = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while loc:
            lx, ly = loc.popleft()
            if maps[lx][ly] == "E":
                return time
            time += 1

            for dx, dy in direction:
                nx, ny = lx + dx, ly + dy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[lx][ly] != "X":
                    visited[nx][ny] = True
                    loc.append([nx, ny])
                
    sx, sy = findStart(maps)
    print(sx, sy)
    adx, ady, time = BFSSToL(maps, sx, sy)
    answer += time
    answer += BFSLToE(adx, ady, maps)
    
    return answer


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))

from collections import deque

def solution(maps):
    def findStart(maps):
        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == "S":
                    return i, j

    def BFSSToL(maps, x, y):
        loc = deque([(x, y)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = True
        time = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while loc:
            for _ in range(len(loc)):  # 같은 레벨의 모든 노드 처리
                lx, ly = loc.popleft()
                if maps[lx][ly] == "L":
                    return lx, ly, time
                for dx, dy in direction:
                    nx, ny = lx + dx, ly + dy
                    if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        loc.append((nx, ny))
            time += 1  # 같은 레벨의 모든 노드를 탐색한 후에만 +1

        return None, None, -1  # 도착 못 하면 -1 반환

    def BFSLToE(x, y):
        loc = deque([(x, y)])
        visited = [[False] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = True
        time = 0
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while loc:
            for _ in range(len(loc)):  # 같은 레벨의 모든 노드 처리
                lx, ly = loc.popleft()
                if maps[lx][ly] == "E":
                    return time
                for dx, dy in direction:
                    nx, ny = lx + dx, ly + dy
                    if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != "X":
                        visited[nx][ny] = True
                        loc.append((nx, ny))
            time += 1  # 같은 레벨의 모든 노드를 탐색한 후에만 +1

        return -1  # 목적지까지 못 가면 -1 반환

    sx, sy = findStart(maps)
    if sx is None or sy is None:
        return -1  # 시작점이 없으면 -1 반환

    adx, ady, time = BFSSToL(maps, sx, sy)
    if time == -1:
        return -1  # L까지 도달할 수 없으면 -1 반환

    e_time = BFSLToE(adx, ady)
    if e_time == -1:
        return -1  # E까지 도달할 수 없으면 -1 반환

    return time + e_time  # S -> L + L -> E 최단 시간 합산


# 테스트
print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))