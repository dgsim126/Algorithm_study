# 옛날 닌텐도 포켓몬 빙판길 문제
# bfs로 풀어야 하는데 is_arrived 대신 왔던 방향으로 되돌아가야하는 경우만 남았다면 종료

from collections import deque

def solution(board):
    start_x= -1
    start_y= -1

    # 시작위치 R 찾기
    for i in range(len(board)):
        print(board[i])
        if "R" in board[i]:
            start_x= i
            start_y= board[i].index("R")
            break

    # print(start_x, start_y)

    queue= deque()
    queue.append((start_x, start_y, 0))

    def bfs(queue, row, column):
        while(queue):
            x, y, cnt= queue.popleft()
            flag= False
            temp_x = x
            temp_y = y

            # 탈출 조건
            if(board[x][y]== "G"):
                return cnt

            # 위 방향
            while(x!=0 and board[x-1][y]=="."):
                flag= True
                temp_x-=1

            if(flag==True):
                queue.append((temp_x, temp_y, cnt+1))
                flag = False
                temp_x = x
                temp_y = y

            # 아래 방향
            while(x<column and board[x+1][y]=="."):
                flag = True
                temp_x += 1

            if (flag == True):
                queue.append((temp_x, temp_y, cnt+1))
                flag = False
                temp_x = x
                temp_y = y

            # 오른쪽 방향
            while(y<row and board[x][y+1]=="."):
                flag = True
                temp_y+=1

            if (flag == True):
                queue.append((temp_x, temp_y, cnt+1))
                flag = False
                temp_x = x
                temp_y = y

            # 왼쪽 방향
            while(y!=0 and board[x][y-1]=="."):
                flag = True
                temp_y -= 1

            if (flag == True):
                queue.append((temp_x, temp_y, cnt+1))
                flag = False
                temp_x = x
                temp_y = y


    bfs(queue, len(board[0]), len(board))

def gpt_solution():
    from collections import deque

    def solution(board):
        n = len(board)  # 세로 크기
        m = len(board[0])  # 가로 크기

        # 시작 위치(R)와 목표 위치(G) 찾기
        start_x, start_y = -1, -1
        goal_x, goal_y = -1, -1
        for i in range(n):
            if "R" in board[i]:
                start_x, start_y = i, board[i].index("R")
            if "G" in board[i]:
                goal_x, goal_y = i, board[i].index("G")

        # 방향 벡터 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS 초기 설정
        queue = deque([(start_x, start_y, 0)])  # (x좌표, y좌표, 이동 횟수)
        visited = set()  # 방문한 좌표 저장
        visited.add((start_x, start_y))

        # BFS 실행
        while queue:
            x, y, count = queue.popleft()

            # 목표 지점 도착 시 반환
            if (x, y) == (goal_x, goal_y):
                return count

            # 4방향 이동
            for dx, dy in directions:
                nx, ny = x, y

                # 벽이나 장애물('D')을 만날 때까지 이동
                while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != "D":
                    nx += dx
                    ny += dy

                # 방문하지 않은 곳이면 큐에 추가
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, count + 1))

        return -1  # 도달할 수 없는 경우


## main ##
board= ["...D..R",
        ".D.G...",
        "....D.D",
        "D....D.",
        "..D...."]
print(solution(board))