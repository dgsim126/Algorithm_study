from collections import deque
def solution(maps):
    answer = []
    N, M = len(maps), len(maps[0])
    dx, dy = [-1,1,0,0], [0,0,-1,1]
    visited = [[False]*M for _ in range(N)]
    
    def bfs(x,y):
        visited[x][y]=True
        queue = deque()
        queue.append((x,y))
        days=int(maps[x][y])
        while queue:
            x,y=queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and maps[nx][ny] != 'X':
                    queue.append((nx,ny))
                    days += int(maps[nx][ny])
                    visited[nx][ny]=True
        return days
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i,j))
    if len(answer)==0:
        return [-1]
    else:
        return sorted(answer)
