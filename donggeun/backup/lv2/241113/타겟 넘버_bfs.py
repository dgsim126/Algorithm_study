from collections import deque

def solution(numbers, target):
    queue= deque()
    queue.append((0, 0)) # depth, current_sum
    cnt= 0

    while(queue):
        depth, current_sum= queue.popleft()

        if (depth == len(numbers)):
            if (current_sum == target):
                cnt += 1
        else:
            queue.append((depth+1, current_sum + numbers[depth]))
            queue.append((depth+1, current_sum - numbers[depth]))

    return cnt


# main
numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))
