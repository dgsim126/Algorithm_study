from itertools import combinations

def solution(numbers):
    answer = []
    for comb in combinations(numbers, 2):
        answer.append(sum(comb))
        
    return sorted(list(set(answer)))