from itertools import permutations

def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set()

    # gpt : 모든 숫자 조합 생성
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            num = int("".join(perm))
            num_set.add(num) # 중복 순열 방지

    # 소수 개수 세기
    count = 0
    for num in num_set:
        if is_prime(num):
            count += 1

    return count