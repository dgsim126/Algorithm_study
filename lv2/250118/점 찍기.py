# 역시나 시간초과
def solution(k, d):
    total_points = 0

    for x in range(0, d + 1, k):
        for y in range(0, d + 1, k):
            if x ** 2 + y ** 2 <= d ** 2:
                total_points += 1

    return total_points

# 야무지다
def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        max_y = int((d ** 2 - x ** 2) ** 0.5) # y의 최대값 계산
        # y는 k만큼씩 증가하므로, 최대값 구하면 y가 몇개인지 구할 수 있다.
        answer += (max_y // k) + 1 # +1은 0

    return answer