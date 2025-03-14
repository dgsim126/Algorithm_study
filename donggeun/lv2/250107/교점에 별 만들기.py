# gpt's help
def solution(line):
    points = set()  # 교점 저장
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A, B, C = line[i]
            D, E, F = line[j]
            denominator = A * E - B * D
            if denominator == 0:  # 평행하거나 일치
                continue
            # 교점 계산
            x_numerator = B * F - C * E
            y_numerator = C * D - A * F
            if x_numerator % denominator == 0 and y_numerator % denominator == 0: # 이 부분이 핵심!!
                x = x_numerator // denominator
                y = y_numerator // denominator
                points.add((x, y))

    # 정수 교점의 최소, 최대값 계산
    x_min = min(x for x, y in points)
    x_max = max(x for x, y in points)
    y_min = min(y for x, y in points)
    y_max = max(y for x, y in points)

    # 격자판 생성
    height = y_max - y_min + 1
    width = x_max - x_min + 1
    grid = [['.'] * width for _ in range(height)]

    for x, y in points:
        grid[y_max - y][x - x_min] = '*'

    # 문자열 결과 반환
    return [''.join(row) for row in grid]


## 테스트
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
