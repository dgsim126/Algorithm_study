def solution(sizes):
    a=0
    b=0
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
        if a < size[0]:
            a = size[0]
        if b < size[1]:
            b = size[1]
    return a * b