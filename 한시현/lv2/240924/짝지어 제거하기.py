def solution(s):
    check = []
    
    for a in s:
        if check:
            if check[-1] == a:
                check.pop()
        else:
            check.append(a)
    
    if not check:
        return 1
    else:
        return 0