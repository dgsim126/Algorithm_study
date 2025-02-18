def solution(priorities, location):
    index = 0

    prior = priorities[location]
    prev = priorities[0:location]
    if location < len(priorities) - 1:
        next = priorities[location + 1:]
    else:
        next = []

    count = 0
    bigger = False
    for i in range(len(next)):
        if not bigger and next[i] > prior:
            bigger = True
            index += 1
        if bigger and next[i] > prior:
            index += 1
            count = 0
        elif bigger and next[i] == prior:
            count += 1

    if not bigger:
        index += 1
    
    prev_count = 0
    for j in range(len(prev)):
        if prev[j] > prior:
            index += 1
            prev_count = 0
        elif prev[j] == prior:
            prev_count += 1

    return index + count + prev_count

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
        

