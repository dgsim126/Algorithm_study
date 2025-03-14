import math

def solution(progresses, speeds):
    answer = [1]
    period = []
    a = math.ceil((100 - (progresses[0]))/speeds[0])
    period.append(a)
    for i in range(1, len(progresses)):
        t = math.ceil((100 - (progresses[i]))/speeds[i])
        if t < period[i-1]:
            answer[-1] = answer[-1] + 1
            period.append(period[i-1])
        elif t > period[i-1]:
            answer.append(1)
            period.append(t)
        else:
            answer[-1] = answer[-1] + 1
            period.append(t)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))