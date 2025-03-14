## 2, 3으로 소인수 분해 먼저 진행하고, n으로 맞추기 > 입출력 예 2의 경우 이상한 결과


from collections import deque


def solution(x, y, n):
    # BFS를 위한 큐 초기화 (현재 숫자, 연산 횟수)
    queue = deque([(x, 0)])
    # 방문 여부를 저장하는 집합
    visited = set()
    visited.add(x)

    while queue:
        current, steps = queue.popleft()

        # y에 도달하면 연산 횟수 반환
        if current == y:
            return steps

        # 가능한 연산 수행
        for next_num in (current + n, current * 2, current * 3):
            # 다음 숫자가 y를 넘지 않고, 방문하지 않았다면 큐에 추가
            if next_num <= y and next_num not in visited:
                visited.add(next_num)
                queue.append((next_num, steps + 1))

    # y에 도달할 수 없는 경우 -1 반환
    return -1

