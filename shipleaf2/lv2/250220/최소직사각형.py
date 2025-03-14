def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        if size[0] >= size[1]:
            w = size[0]
            h = size[1]
        else:
            w = size[1]
            h = size[0]
        
        if w > max_w:
            max_w = w
        if h > max_h:
            max_h = h

    return max_w * max_h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
