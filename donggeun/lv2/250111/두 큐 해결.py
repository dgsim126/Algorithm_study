from collections import deque

# gpt
def solution(queue1, queue2):
    # 두 큐의 합 계산
    total_sum = sum(queue1) + sum(queue2)
    if total_sum % 2 != 0:  # 합이 홀수라면 균등 분배 불가능
        return -1

    target = total_sum // 2  # 각 큐가 가져야 하는 합
    combined = queue1 + queue2  # 순환 큐를 위한 리스트
    n = len(queue1)

    # 슬라이딩 윈도우 초기화
    current_sum = sum(queue1)
    left, right = 0, n
    min_operations = float('inf')

    while left < 2 * n and right < 2 * n:
        if current_sum == target:  # 목표 합 달성
            min_operations = min(min_operations, left + (right - n))
            break
        elif current_sum < target:  # 더 큰 합이 필요
            if right < 2 * n:
                current_sum += combined[right % (2 * n)]
                right += 1
        else:  # 합이 너무 크다면
            current_sum -= combined[left % (2 * n)]
            left += 1

    return min_operations if min_operations != float('inf') else -1
