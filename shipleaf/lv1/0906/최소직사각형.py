def solution(sizes):
    answer = 0
    width = 0
    height = 0

    for i in sizes:
        if i[1] > i[0]:
            i.reverse()
        if i[0] >= width:
            width = i[0]
        if i[1] >= height:
            height = i[1]
    answer = width * height
    return answer