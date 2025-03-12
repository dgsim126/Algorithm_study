# 시간 초과
def solution(n, left, right):
    # matrix = [[0 for _ in range(n)] for _ in range(n)]
    #
    # for i in range(n):
    #     for j in range(n):
    #         matrix[i][j] = max(i + 1, j + 1)

    matrix = [[max(i+1,j+1) for i in range(n)] for j in range(n)]

    flat = []
    for row in matrix:
        for col in row:
            flat.append(col)

    return flat[left:right+1]

# gpt
def solution(n, left, right):
    result = []

    # left부터 right까지 필요한 값만 계산
    for index in range(left, right + 1):
        i = index // n  # 행 번호
        j = index % n   # 열 번호
        result.append(max(i + 1, j + 1))

    return result
