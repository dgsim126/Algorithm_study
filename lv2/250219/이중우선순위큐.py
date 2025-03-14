# I 숫자 : 큐에 숫자 삽입, D 1 : 큐에서 최댓값 삭제, D -1 : 큐에서 최솟값 삭제
# 최대 힙?
# gpt
import heapq

def solution(operations):
    minheap = []  # 최소 힙 (최솟값을 빠르게 찾기)
    maxheap = []  # 최대 힙 (최댓값을 빠르게 찾기)
    element_count = {}  # 실제 존재하는 값 개수를 저장 (삭제 동기화용)

    for oper in operations:
        op, num = oper.split()
        num = int(num)

        if op == "I":  # 삽입 연산
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)  # 최대 힙은 음수로 저장
            element_count[num] = element_count.get(num, 0) + 1  # 원소 개수 기록

        elif op == "D" and element_count:  # 삭제 연산 (큐가 비었으면 무시)
            if num == 1:  # 최댓값 삭제
                while maxheap:
                    max_value = -heapq.heappop(maxheap)
                    if element_count.get(max_value, 0) > 0:  # 실제 존재하는 값이면 삭제
                        element_count[max_value] -= 1
                        if element_count[max_value] == 0:
                            del element_count[max_value]
                        break
            else:  # num == -1, 최솟값 삭제
                while minheap:
                    min_value = heapq.heappop(minheap)
                    if element_count.get(min_value, 0) > 0:  # 실제 존재하는 값이면 삭제
                        element_count[min_value] -= 1
                        if element_count[min_value] == 0:
                            del element_count[min_value]
                        break

    if not element_count:  # 모든 값이 삭제된 경우
        return [0, 0]

    # 남아 있는 숫자 중 최댓값과 최솟값 찾기
    while maxheap:
        max_value = -heapq.heappop(maxheap)
        if max_value in element_count:
            break

    while minheap:
        min_value = heapq.heappop(minheap)
        if min_value in element_count:
            break

    return [max_value, min_value]