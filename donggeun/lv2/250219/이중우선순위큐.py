"""
최소힙을 구하는 건 heapq를 사용하면 될 거 같은데, 최대힙은 어떻게 구하지?
최소힙에서 최소값 제외한 후 최소힙 안에 값을 전부 음수로 바꿔서 최대힙을 구해??g
"""
import heapq


# 최대힙, 최소힙 변환
def convert(heap):
    result = []
    for val in heap:
        result.append(-val)

    heapq.heapify(result)
    return result


def solution(operations):
    queue = []
    heapq.heapify(queue)

    for i in range(len(operations)):
        oper, num = operations[i].split(" ")
        num = int(num)
        if (oper == "I"):
            heapq.heappush(queue, num)


        elif (len(queue) > 0):
            if (num == 1):  # 큐에서 최댓값 삭제
                queue = convert(queue)
                heapq.heappop(queue)
                queue = convert(queue)


            else:  # 큐에서 최솟값 삭제
                heapq.heappop(queue)

    # 결과 반환
    if (len(queue) <= 0):
        return [0, 0]
    else:
        min_ = queue[0]
        queue = convert(queue)
        max_ = queue[0]
        return [-max_, min_]
