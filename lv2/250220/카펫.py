def solution(brown, yellow):
    square = brown + yellow

    for i in range (1, square):
        if square % i == 0:
            j = square // i

            if (i - 2) * (j - 2) == yellow:
                if i > j:
                    return [i, j]
                else:
                    return [j, i]