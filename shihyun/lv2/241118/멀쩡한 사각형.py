# gpt
from math import gcd

def solution(W, H):
    # 전체 정사각형 개수
    total = W * H
    # 잘리는 정사각형 개수
    cut = W + H - gcd(W, H)
    # 사용할 수 있는 정사각형 개수

    return total - cut