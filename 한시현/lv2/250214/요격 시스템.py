def solution(targets):
    missile = 0
    targets.sort(key = lambda x: x[1])

    x_end = 0
    for target in targets:
        if target[0] < x_end: # 폭격 시작 < 요격 끝
            continue

        else:
            missile += 1
            x_end = target[1]

    return missile