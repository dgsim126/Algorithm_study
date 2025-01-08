# gpt
def solution(line):
    # 1. 모든 교점 계산
    points = set() # 정수 교점 저장하는 집합
    n = len(line)

    for i in range(n):
        for j in range(i + 1, n):
            # 두 직선의 조합을 전부 구함
            A1, B1, C1 = line[i]
            A2, B2, C2 = line[j]

            determinant = A1 * B2 - A2 * B1

            # 두 직선이 평행한 경우 (=0 일 경우)
            if determinant == 0:
                continue

            # 교점 계산 (=0 아닌 경우)
            x_numerator = B1 * C2 - B2 * C1
            y_numerator = A2 * C1 - A1 * C2

            # 좌표 계산
            if x_numerator % determinant == 0 and y_numerator % determinant == 0: # x와 y가 정수 좌표인지 확인하기 위해 분자를 분모로 나눌 수 있는지 검사
                x = x_numerator // determinant
                y = y_numerator // determinant
                points.add((x, y)) # 정수 교점 저장

    # 2. 격자판 범위 계산
    if not points: # 정수 교점 없으면 빈 리스트 반환
        return []

    # x좌표, y좌표 추출해서 리스트로 저장
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]
    # 최소, 최대 x,y 좌표 계산
    min_x, max_x = min(x_coords), max(x_coords)
    min_y, max_y = min(y_coords), max(y_coords)

    # 3. 격자판 초기화
    height = max_y - min_y + 1
    width = max_x - min_x + 1
    grid = [['.'] * width for _ in range(height)]

    # 4. 별 찍기
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'

    # 5. 문자열로 변환하여 반환
    return [''.join(row) for row in grid]