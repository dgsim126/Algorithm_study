from collections import deque

def solution(priorities, location):
    q = deque([(i, priorities[i]) for i in range(len(priorities))]) # gpt
    check = 0

    while q:
        get = q.popleft()
        hasbigger = False

        for left in q:
            if left[1] > get[1]:
                hasbigger = True
                break

        if hasbigger:
            q.append(get)
        else:
            check += 1
            if get[0] == location:
                return check