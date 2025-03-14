from collections import deque

def solution(maps):
    x_len= len(maps[0])
    y_len= len(maps)

    dx= [1, 0, -1, 0] # 동, 남, 서, 북
    dy= [0, 1, 0, -1] # 동, 남, 서, 북

    queue= deque()

    queue.append((0, 0))

    while(queue):
        x, y= queue.popleft()

        # 탈출조건
        if(x==x_len-1 and y==y_len-1):
            return maps[x][y]

        for i in range(4):
            # 새로운 좌표
            new_x= x+dx[i]
            new_y= y+dy[i]

            if(0 <= new_x < x_len and 0 <= new_y < y_len and maps[new_x][new_y]==1):
                maps[new_x][new_y]= maps[x][y]+1
                queue.append((new_x, new_y))

    return -1


## main ##
maps1 = [[1, 0, 1, 1, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1]]


print(solution(maps1))  # 11


