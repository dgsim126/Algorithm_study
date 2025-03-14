from itertools import combinations, permutations


def check(num):
    if (num == 0 or num == 1):
        return 0
    if (num == 2 or num == 3):
        return 1

    if (num % 2 == 0):
        return 0

    # for i in range(2, num//2+1):
    for i in range(2, int(num ** (1 / 2)) + 1):
        if (num % i == 0):
            return 0

    return 1


def solution(numbers):
    number = list(numbers)
    result = []

    for i in range(1, len(number) + 1):
        temp = list(permutations(number, i))
        for j in temp:
            val = "".join(j)
            result.append(int(val))

    print(result)
    result = set(result)
    result = list(result)
    print(result)

    # 이제 result에서 소수의 개수를 찾으면 된다! - 소수인지 어떻게 판단했지? 절반까지 나눠보며 나머지확인