# 현재 사용자 위치를 기준으로 4방위 탐색
def check(whole, a, b, diff, diff_1, diff_2):
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]

    if diff == 0.5:
        return 0
    elif diff == 1.0:
        if diff_1 == diff_2:  # 대각선인 경우
            if (
                a1 + 1 < 5 and a2 + 1 < 5 and
                whole[a1 + 1][a2] == "X" and whole[a1][a2 + 1] == "X"
            ):
                return 1
        else:  # 직선인 경우
            if diff_1 > 0:  # 세로 방향
                if a1 + 1 < 5 and whole[a1 + 1][a2] == "X":
                    return 1
            else:  # 가로 방향
                if a2 + 1 < 5 and whole[a1][a2 + 1] == "X":
                    return 1
        return 0
    else:
        return 0


def distance(whole, a, b):
    a1 = a[0]
    a2 = a[1]
    b1 = b[0]
    b2 = b[1]

    diff_1 = abs(a1 - b1)
    diff_2 = abs(a2 - b2)
    diff = diff_1 + diff_2

    if diff <= 2:
        return check(whole, a, b, diff, diff_1, diff_2)
    else:
        return 1


def solution(places):
    result = []

    for i in range(len(places)):
        whole = [list(row) for row in places[i]]
        lst = []

        for j in range(len(whole)):
            for k in range(len(whole[j])): 
                if whole[j][k] == "P":
                    lst.append([j, k])

        valid = True  # 거리두기 준수 여부
        for j in range(len(lst) - 1):
            for k in range(j + 1, len(lst)):
                first = lst[j]
                last = lst[k]
                if distance(whole, first, last) == 0:
                    valid = False
                    break
            if not valid:
                break

        result.append(1 if valid else 0)

    return result


## main ##
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
