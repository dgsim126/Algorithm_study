def solution(brown, yellow):
    vertical_len = int(brown/2)
    vertical = 0
    for i in range(1, vertical_len):
        horizon = (brown - (2 * i)) / 2
        if (horizon - 2) * i == yellow:
            vertical = i
            break
    
    h = vertical + 2
    w = int((brown + yellow) / h)

    return [w, h]

print(solution(10,2))