# '''
# 대기큐를 계속 정렬된 상태로 유지하는 것이 문제의 가장 중요한 포인트인 것 같음
# - 첫 번째 값(우선순위가 가장 높은 값)만 정확하면 되기에 heapq를 사용하는게 효율적인 것 같은데..
# - 문제는 내가 heapq에 값을 넣을 때, 특정한 어떤 값을 기준으로 heapq를 유지하는 방법을 알지 못함
# 일단 해당 문제 효율성을 확인한다는 내용이 없으니 리스트 정렬 방법으로 구현해보자!
#
# '''
#
# from collections import deque
#
#
# def solution(jobs):
#     wait = deque()
#     time = 0
#     result = []
#
#     for i in range(len(jobs)):
#         jobs[i].append(i)
#
#     print(jobs)
#
#     jobs = deque(jobs)
#
#     while (jobs):
#         # 대기큐에 값 넣기
#         temp_point = 0
#         while (jobs):
#             current = jobs[0]
#             if (current[0] <= time):
#                 current = jobs.popleft()
#                 # print("대기큐에 들어간 값: ", current) # [요청 시간, 작업 시간, 작업 번호]
#                 wait.append(current)
#             else:
#                 # print(f"time={time}이고, current={current}이기에 대기큐에 들어갈 수 없음")
#                 break
#
#         # 대기큐 우선순위 정렬
#         wait = list(wait)
#         wait.sort(key=lambda x: (x[1], x[0], x[2]))
#         wait = deque(wait)
#         # print(f"대기큐 우선순위 정렬: {wait}")
#
#         # 대기큐에서 값을 꺼내 수행하고, 시간 업데이트
#         current = wait.popleft()
#         time += current[1]
#         result.append(time)
#         # print(f"시간 업데이트: {time}")
#
#     return time

import heapq
from collections import deque

def solution(jobs):
    # 1. 작업을 요청 시간(s) 기준으로 정렬
    jobs = deque(sorted(jobs, key=lambda x: x[0]))  # deque로 변환하여 popleft() 최적화
    heap = []  # 우선순위 큐 (작업 시간 기준)
    time, total_turnaround_time = 0, 0
    count = 0  # 완료된 작업 수

    while jobs or heap:
        # 2. 현재 시간(time)까지 요청된 작업을 대기 큐(heap)에 추가
        while jobs and jobs[0][0] <= time:
            request_time, duration = jobs.popleft()
            heapq.heappush(heap, (duration, request_time))  # 작업 시간 기준 최소 힙

        # 3. 실행할 작업 선택
        if heap:
            duration, request_time = heapq.heappop(heap)  # 작업 시간이 짧은 작업 선택
            time += duration  # 현재 시간 갱신 (작업 수행)
            total_turnaround_time += (time - request_time)  # 반환 시간 누적
            count += 1  # 완료된 작업 수 증가
        else:
            # 대기 큐가 비었을 경우, 다음 요청 시간으로 이동
            time = jobs[0][0]

    # 4. 평균 반환 시간 계산 (정수 부분만 반환)
    return total_turnaround_time // count  # 정수 부분만 반환

# 테스트 실행
print(solution([[0, 3], [1, 9], [3, 5]]))  # 8
