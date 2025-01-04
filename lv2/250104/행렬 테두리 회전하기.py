def solution(rows, columns, queries):
    matrix = []
    num = 1

    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(num)
            num += 1
        matrix.append(row)

    result = []

    # gpt
    # 쿼리 처리
    for x1, y1, x2, y2 in queries:
        # 2-1. 1-based index를 0-based index로 변환
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        # 테두리 회전을 위한 첫 번째 값 저장
        temp = matrix[x1][y1]
        min_val = temp

        # 상단 이동
        for col in range(y1, y2):
            matrix[x1][col] = matrix[x1][col + 1]
            min_val = min(min_val, matrix[x1][col])

        # 오른쪽 이동
        for row in range(x1, x2):
            matrix[row][y2] = matrix[row + 1][y2]
            min_val = min(min_val, matrix[row][y2])

        # 하단 이동
        for col in range(y2, y1, -1):
            matrix[x2][col] = matrix[x2][col - 1]
            min_val = min(min_val, matrix[x2][col])

        # 왼쪽 이동
        for row in range(x2, x1, -1):
            matrix[row][y1] = matrix[row - 1][y1]
            min_val = min(min_val, matrix[row][y1])

        # 마지막 복사
        matrix[x1 + 1][y1] = temp

        # 최솟값 저장
        result.append(min_val)

    return result