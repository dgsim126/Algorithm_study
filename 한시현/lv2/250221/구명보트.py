from collections import deque

def solution(people, limit):
    d_p = deque(sorted(people))
    boat = 0

    while d_p:
        if len(d_p) > 1 and d_p[0] + d_p[-1] <= limit:
            d_p.popleft()
        d_p.pop()
        boat += 1

    return boat