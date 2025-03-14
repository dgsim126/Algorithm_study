# gpt's help
import math


def solution(W, H):
    total_squares = W * H

    # 대각선이 지나는 정사각형 개수
    cut_squares = W + H - math.gcd(W, H)

    # 사용할 수 있는 정사각형 개수
    usable_squares = total_squares - cut_squares

    return usable_squares


# 테스트
print(solution(8, 12))  # 출력: 80
