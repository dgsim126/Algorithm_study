import heapq

def solution(scovile, k):
    heapq.heapify(scovile)
    cnt = 0

    while (scovile[0] < k):
        cnt += 1

        # 예외 조건
        if (len(scovile) < 2):
            return -1

        first = heapq.heappop(scovile)
        second = heapq.heappop(scovile)
        heapq.heappush(scovile, first + second * 2)

    return cnt


# def solution(scovile, k): 효율성 실패 (시간초과)
#     cnt = 0
#
#     while (min(scovile) < k):
#         cnt += 1
#
#         # 예외 조건
#         if (len(scovile) < 2):
#             return -1
#
#         first = scovile.pop(scovile.index(min(scovile)))
#         second = scovile.pop(scovile.index(min(scovile)))
#         scovile.append(first + second * 2)
#
#     return cnt