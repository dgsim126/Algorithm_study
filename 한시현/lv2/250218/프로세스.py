def solution(priorities, location):
    q = [[i, priorities[i]] for i in range(len(priorities))]
    check = 0

    while q:
        get = q.pop(0)
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