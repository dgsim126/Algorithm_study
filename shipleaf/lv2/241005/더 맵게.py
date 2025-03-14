def solution(scoville, K):
    answer = 0
    scoville.sort()
    list = []
    list.append(scoville.pop(0))
    while True:
        if list[0] >= K and scoville[0] >= K:
            break
        elif scoville == []:
            return -1
        else:
            if list[0] > scoville[0]:
                list[0], scoville[0] = scoville[0], list[0]
            list[0] = list[0] + (scoville.pop(0) * 2)
            answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))