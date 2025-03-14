# 시간 초과
from itertools import permutations # gpt

def solution(n, k):
    answer = []
    people = [i for i in range(1, n+1)]

    peoplelist = list(permutations(people))

    return peoplelist[k-1]