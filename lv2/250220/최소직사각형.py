def solution(sizes):
    max_a, max_b = 0,0

    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
        if max_a < size[0]:
            max_a = size[0]
        if max_b < size[1]:
            max_b = size[1]

    return max_a * max_b