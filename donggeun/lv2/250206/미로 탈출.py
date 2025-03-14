# 레버 위치 먼저 방문 후, exit을 방문해야 함
# 당연히 bfs
# is_visited 리스트 하나 만들어서 방문 여부 확인
# 현 위치에서 4방향으로 한 칸씩 이동한 후, queue에 삽입
# 모든 통로는 다시 지나갈 수 있으므로, 레버를 찾을때까지 최단거리, 출구를 찾을때까지 최단거리
# 2번 시행해야 함. 즉 is_visited를 레버를 찾은 시점에서 초기화!

from collections import deque

def solution(maps):
    map= [list(row) for row in maps]
    is_visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    start_x = -1
    start_y = -1

    # 시작 위치 S 찾기
    for i in range(len(maps)):
        if "S" in maps[i]:
            start_x, start_y = i, maps[i].index("S")
            break

    first_queue= deque()
    first_queue.append((start_x, start_y, 0))  # 시작위치, 이동거리

    x_move= [-1, 0, 1, 0] # 북 동 남 서
    y_move= [0, 1, 0, -1] # 북 동 남 서

    def bfs(value, queue):
        while(queue):
            x, y, distance= queue.popleft()
            # print(x, y, distance)

            if(map[x][y]==value):
                return x, y, distance # 레버까지의 최단거리

            for i in range(4):
                next_x= x+x_move[i]
                next_y= y+y_move[i]
                if(0<=next_x<len(maps) and 0<=next_y<len(maps[0]) and is_visited[next_x][next_y]==False and map[next_x][next_y] != "X"):
                    is_visited[next_x][next_y]= True
                    queue.append((next_x, next_y, distance+1))
        return -1, -1, -1

    second_x, second_y, distance= bfs("L", first_queue)
    if(distance==-1):
        return -1
    print(second_x, second_y, distance)


    # 레버에서 목적지까지!
    map = [list(row) for row in maps]  # 맵을 2차원 리스트로 변환
    is_visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    second_queue= deque()
    second_queue.append((second_x, second_y, distance))

    last_x, last_y, distance= bfs("E", second_queue)
    print(last_x, last_y, distance)
    if (distance == -1):
        return -1
    return distance

## main ##
maps= ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))