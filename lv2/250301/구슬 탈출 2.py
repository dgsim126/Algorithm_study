from collections import deque

def solution(N, M, board):
    row, col = len(board), len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                red = (i, j)
            elif board[i][j] == "B":
                blue = (i, j)

    def bfs():
        queue = deque([(red, blue, 0)])
        visited = [[False] * col] * row
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            r_pos, b_pos, count = queue.popleft()
            r_x, r_y = r_pos
            b_x, b_y = b_pos
            
            if count > 10:
                return -1

            for dx, dy in direction:
                is_red = False
                is_blue = False
                while True:
                    if board[r_x + dx][r_y + dy] != "#":
                        r_x += r_x + dx
                        r_y += r_y + dy

                        if board[r_x][r_y] == "O":
                            is_blue = True
                            break
                    else:
                        break

                while True:
                    if board[b_x + dx][b_y + dy] != "#":
                        b_x += b_x + dx
                        b_y += b_y + dy

                        if board[r_x][r_y] == "O":
                            is_blue = True
                            break
                    else:
                        break
            
            if is_red and not is_blue:
                return count + 1
            elif not is_red and not is_blue and not visited[r_x][r_y]:
                queue.append([[r_x, r_y], [b_x, b_y], count + 1])
                visited[r_x][r_y] = True

        return -1

    return bfs()
                
board = ["#####", "#..B#", "#.#.#", "#RO.#", "#####"]
print(solution(5, 5, board))


# N, M = map(int, input().split())
# board = [list(input().strip()) for _ in range(N)]

# print(solution(N, M, board))