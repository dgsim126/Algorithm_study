from collections import deque

def solution(scoville, K):
    sorted_scoville = sorted(scoville)
    stack = []
    for i in range(len(sorted_scoville)):
        if sorted_scoville[i] < K:
            stack.append(sorted_scoville[i])
    
    if len(sorted_scoville) == 0:
        return 0
    elif len(sorted_scoville) == 1:
        return 1
    
    stack = sorted(stack)

    count = 0
    while stack:
        if len(stack) == 1:
            count += 1
            return count
        
        first = stack.pop[0]
        second = stack.pop[0]

        new  = (second * 2)
    
    

print(solution([1, 2, 3, 9, 10, 12], 7))