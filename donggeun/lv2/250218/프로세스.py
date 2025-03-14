from collections import deque


def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (우선순위, 인덱스) 저장
    print(queue)
    count = 0  # 실행 순서 카운트

    while queue:
        current = queue.popleft()  # 맨 앞 프로세스 꺼내기

        # 현재 프로세스보다 높은 우선순위가 있는지 확인
        if any(current[0] < q[0] for q in queue):
            queue.append(current)  # 우선순위가 더 높은 게 있으면 다시 큐에 삽입(다시 뒤에 넣는구나....)
        else:
            count += 1  # 실행된 프로세스 수 증가
            if current[1] == location:  # 우리가 찾던 프로세스면 실행 순서 반환
                return count






