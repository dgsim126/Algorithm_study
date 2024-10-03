def solution(progresses, speeds):
    deploy = []
    days = 0

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        if count > 0:
            deploy.append(count)

    return deploy