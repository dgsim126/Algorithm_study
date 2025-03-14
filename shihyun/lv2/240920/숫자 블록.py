# 미완
def solution(begin, end):
    road = [0 for _ in range(begin, end+1)]
    block = 1

    while block <= end:    
        for i in range(1,end):
            if block * i > end:
                road[block * i] = block

        block += 1

    return road[begin:]