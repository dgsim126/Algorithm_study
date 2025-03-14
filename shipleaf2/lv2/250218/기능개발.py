from collections import deque

def solution(progresses, speeds):
    queue = deque()
    answer = []
    for i in range(len(progresses)):
        if not queue:
            answer.append(1)
            time = (100-progresses[i])/speeds[i]
            if time != int(time):
               time = int(time) + 1
            queue.append(time)
        else:
            day = (100-progresses[i])/speeds[i]
            if day != int(day):
                day = int(day) + 1
            prev_day = queue.popleft()
            if day <= prev_day:
                answer[-1] += 1
                queue.append(prev_day)
            else:
                answer.append(1)
                queue.append(day)
            print(answer)

    return answer

print(solution([93,30,55],[1,30,5]))
    