from collections import deque

def solution(x, y, n):

    queue = deque([[x, 0]])
    visted = set()

    while queue:
        current, steps = queue.popleft()

        if current == y:
            return steps
        
        if current in visted:
            continue
        visted.add(current)
        
        if current + n <= y:
            queue.append((current + n, steps + 1))
        if current * 2 <= y:
            queue.append((current * 2, steps + 1))
        if current * 3 <= y:
            queue.append((current * 3, steps + 1))
    
    return -1


print(solution(10, 40, 5))