'''
순서대로 배포되어야 함
- while을 돌면서 현재 진행률에 하루에 개발 가능한 진행률을 더한다.
- 만약 progresses 가장 앞의 값이 100 이상이 되었다면 popleft한다.
-- 이때, popleft를 할 수 있는 만큼 진행하고 popleft한 횟수를 저장한다.
'''
from collections import deque


def solution(progresses, speeds):
    result = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while (progresses):
        # 오늘 개발 분량 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 개발 완료되었는지 확인
        cnt = 0
        while (len(progresses) > 0 and progresses[0] >= 100):
            cnt += 1
            progresses.popleft()
            speeds.popleft()

        if (cnt != 0):
            result.append(cnt)

    print(result)
    return result


## main ##
progresses = [95, 90, 99, 99, 80, 99]  # 현재 진행률
speeds = [1, 1, 1, 1, 1, 1]  # 하루에 개발 가능한 진행률
print(solution(progresses, speeds))