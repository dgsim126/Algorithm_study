from collections import deque


def solution(arr):
    if (len(arr) == 0):
        return []

    result = []
    arr = deque(arr)

    before = arr.popleft()
    result.append(before)

    while (arr):
        temp = arr.popleft()
        if (temp == before):
            continue
        else:
            before = temp
            result.append(before)

    return result


## main ##
arr = [4, 4, 4, 3, 3]
print(solution(arr))