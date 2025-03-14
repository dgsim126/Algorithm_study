from itertools import combinations

def solution(number):
    answer = []
    arr = []
    count = 0
    for comb in combinations(number, 2):
        arr.append(sum(comb))
    
    arr.sort()

    answer.append(arr[0])
    for i in range(0, len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])

    return answer

