from collections import deque

def solution(progresses, speeds):
    # while문을 돌며 현재 진행률에 하루 개발 가능한 진행률을 더한다.
    # 이때 이미 100을 넘긴 경우는 더하지 않는다.
    # progresses.popleft의 값이 100을 넘겼다면 해당 큐를 조회하며 100인 녀석들을 한방에 제거
    # 총 몇개가 제거되었는지 기록

    progresses= deque(progresses)
    speeds= deque(speeds)
    answer= []

    while(len(progresses)!=0):
        # 하루 분량 업데이트
        for i in range(len(progresses)):
            if(progresses[i]<100):
                progresses[i]+= speeds[i]

        # 맨 앞이 100%가 되었는지 확인
        cnt= 1
        if(progresses[0]>=100):
            progresses.popleft()
            speeds.popleft()

            for i in range(len(progresses)):
                if(progresses[0]>=100):
                    progresses.popleft()
                    speeds.popleft()
                    cnt+=1
                else:
                    break
            answer.append(cnt)

    return answer


## main ##
progresses= [95, 90, 99, 99, 80, 99] # 현재 진행률
speeds= [1, 1, 1, 1, 1, 1] # 하루에 개발 가능한 진행률
print(solution(progresses, speeds))