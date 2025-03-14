# GPT

from collections import deque

def is_safe(place):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                queue = deque([(i, j, 0)])
                visited = set()
                visited.add((i, j))
                
                while queue:
                    x, y, dist = queue.popleft()
                    if dist >= 1 and dist <= 2 and place[x][y] == 'P':
                        return False
                    
                    if dist < 2:
                        for dx, dy in directions:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                                if place[nx][ny] != 'X':
                                    queue.append((nx, ny, dist + 1))
                                    visited.add((nx, ny))
    return True

def solution(places):
    result = []
    for place in places:
        result.append(1 if is_safe(place) else 0)
    return result