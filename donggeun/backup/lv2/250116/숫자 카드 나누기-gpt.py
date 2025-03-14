import math
from functools import reduce

# 최대공약수 구하기
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 리스트의 최대공약수
def find_gcd(arr):
    return reduce(gcd, arr)

# 공약수 구하기
def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors, reverse=True)

# 조건에 맞는 최대 공약수 찾기
def find_valid_gcd(arrayA, arrayB):
    gcd_A = find_gcd(arrayA)  # arrayA의 최대공약수
    divisors_A = get_divisors(gcd_A)  # arrayA 최대공약수의 모든 약수

    for d in divisors_A:
        if all(b % d != 0 for b in arrayB):  # arrayB의 모든 원소가 d로 나눠지지 않는지 확인
            return d

    return 0

def solution(arrayA, arrayB):
    result1 = find_valid_gcd(arrayA, arrayB)  # 조건 1 확인
    result2 = find_valid_gcd(arrayB, arrayA)  # 조건 2 확인
    return max(result1, result2)

# 테스트
arrayA = [10, 20]
arrayB = [5, 17]
print(solution(arrayA, arrayB))  # 출력: 10