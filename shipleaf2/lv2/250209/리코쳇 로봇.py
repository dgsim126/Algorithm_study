# from collections import deque

# def solution(board):
#     row = len(board)
#     col = len(board[0])

#     def findStart(board):
#         for i in range(row):
#             for j in range(col):
#                 if board[i][j] == "R":
#                     return i, j
                
#     def bfs(rx, ry, board):
#         queue = deque([(rx, ry)])
#         visited = [[False] * col for _ in range(row)]
#         direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#         visited[rx][ry] = True
#         time = 0
        
#         while queue:
#             for _ in range(len(queue)):
#                 x, y = queue.popleft()
#                 if board[x][y] == "G":
#                     return time
#                 for dx, dy in direction:
#                     nx = x + dx
#                     ny = y + dy
#                     if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny] != "D":
#                         if dx == -1:
#                         if dx == 1:
#                         if dy == -1:
#                         if dy == 1:

#                         queue.append((nx, ny))
#                         visited[x][y] = True
#             time += 1

#         return -1
    
#     rx, ry = findStart(board)
#     return bfs(rx, ry, board)

from collections import deque

def solution(board):
    row, col = len(board), len(board[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                start_x, start_y = i, j

    queue = deque([(start_x, start_y, 0)])
    visited = [[False] * col for _ in range(row)]
    visited[start_x][start_y] = True
    
    while queue:
        x, y, moves = queue.popleft()
        
        if board[x][y] == "G":
            return moves

        for dx, dy in direction:
            nx, ny = x, y

            while 0 <= nx + dx < row and 0 <= ny + dy < col and board[nx + dx][ny + dy] != "D":
                nx += dx
                ny += dy

            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))