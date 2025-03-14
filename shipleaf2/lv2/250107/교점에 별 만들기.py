# def solution(line):
#     intersection = []
#     min_X = 100000
#     min_Y = 100000
#     max_X = -100000
#     max_Y = -100000
#     for i in range(len(line)):
#         x1, y1, z1 = line[i]
#         for j in range(i+1, len(line)):
#             x = 0
#             y = 0
#             x2, y2, z2 = line[j]
#             if x1 == 0:
#                 y = -1 * (z1/y1)
#                 x = (-1 * (y2 * y + z2)) * (1/x2)
#             elif y1 == 0:
#                 x = -1 * (z1/x1)
#                 y = (-1 * (x2 * x + x2)) * (1/y2)
#             elif x2 == 0:
#                 y = -1 * (z2/y2)
#                 x = x = (-1 * (y1 * y + z1)) * (1/x1)
#             elif y2 == 0:
#                 x = -1 * (z2/x2)
#                 y = (-1 * (x1 * x + x1)) * (1/y1)
#             else:
#                 x2 = x2 * (x1/x2)
#                 y2 = y2 * (x1/x2)
#                 z2 = z2 * (x1/x2)

#                 y2 = y2 - y1
#                 z2 = z2 - z1

#                 if z2 == 0:
#                     y = 0
#                     x = -1 * (z1/x1)
#                 else:
#                     z2 = z2 * (1/y2)
                    
#                     y = -1 * z2
#                     x = (-1 * (y1 * y + z1)) * (1/x1)

#             if x == int(x) and y == int(y):
#                 if x < min_X:
#                     min_X = int(x)
#                 if y < min_Y:
#                     min_Y = int(y)
#                 if x > max_X:
#                     max_X = int(x)
#                 if y > max_Y:
#                     max_Y = int(y)
#                 intersection.append([x,y])
#     # print(max_X, max_Y, min_X, min_Y)
#     print(intersection)
#     answer = ["." * (abs(max_X-min_X) + 1) for _ in range(abs(max_Y - min_Y))]
    

#     return answer

# print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))


def solution(line):
    # 모든 직선의 교점을 구하는 함수
    def find_intersection(line1, line2):
        A1, B1, C1 = line1
        A2, B2, C2 = line2
        determinant = A1 * B2 - A2 * B1
        
        if determinant == 0:  # 평행하거나 일치하는 경우
            return None
        
        # 교점 좌표 계산
        x = (B1 * C2 - B2 * C1) / determinant
        y = (A2 * C1 - A1 * C2) / determinant
        
        # 정수 좌표인지 확인
        if x.is_integer() and y.is_integer():
            return int(x), int(y)
        return None
    
    # 모든 직선 쌍의 교점 찾기
    points = set()
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            intersection = find_intersection(line[i], line[j])
            if intersection:
                points.add(intersection)
    
    # 교점이 없는 경우
    if not points:
        return []
    
    # 교점의 범위 계산
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    
    # 결과 문자열 생성
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [['.'] * width for _ in range(height)]
    
    for x, y in points:
        grid[max_y - y][x - min_x] = '*'  # 좌표 변환
    
    return [''.join(row) for row in grid]