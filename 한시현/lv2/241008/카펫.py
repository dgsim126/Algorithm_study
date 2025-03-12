def solution(brown, yellow):
    square = brown + yellow

    for i in range (1, int(square ** 0.5) + 1):
        j = square // i

        if square % i == 0:
            if (i - 2) * (j - 2) == yellow:
                if i > j:
                    return [i, j]
                else:
                    return [j, i]