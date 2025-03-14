## https://www.youtube.com/watch?v=0bqfTzpWySY
def solution(triangle):
    # 삼각형의 높이
    n = len(triangle)

    # 아래에서부터 거슬러 올라가면서 최댓값 계산
    for i in range(n - 2, -1, -1):  # 아래에서 두 번째 줄부터 시작
        for j in range(len(triangle[i])):  # 현재 줄의 모든 원소에 대해
            # 아래층 두 개 중 더 큰 값을 선택하여 현재 위치에 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

    # 꼭대기의 값이 최대 경로 합
    return triangle[0][0]