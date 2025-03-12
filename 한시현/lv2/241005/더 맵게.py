# 시간 초과
def solution(scoville, K):
    count = 0

    while len(scoville) > 1:
        scoville.sort()
        new = scoville.pop(0) + scoville.pop(0)*2
        scoville = [new] + scoville
        count += 1

        if min(scoville) >= K:
            return count

    return -1

# from collections import deque
# def solution(scoville, K):
#     sdq = deque(sorted(scoville))
#     allclear = False

#     count = 0
#     while not allclear:
#         count += 1
#         new = sdq.popleft() + sdq.popleft()*2
#         sdq.appendleft(new)

#         for check in sdq:
#             if K > check:
#                 break
#             if check == sdq[-1]:
#                 allclear = True
                
#     return count