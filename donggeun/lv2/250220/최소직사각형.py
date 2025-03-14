def solution(sizes):
    big = []
    small = []

    for i in range(len(sizes)):
        a, b = sizes[i]
        if (a > b):
            big.append(a)
            small.append(b)
        else:
            big.append(b)
            small.append(a)

    return max(big) * max(small)