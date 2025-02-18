from collections import deque

def solution(prices):
    stack = deque([])
    answer = [0] * len(prices)
    for i in range(len(prices)):
        if not stack:
            stack.append([prices[i], i])
        else:
            while stack:
                prev_price, index = stack[-1]
                if prices[i] < prev_price:
                    answer[index] = i - index
                    stack.pop()
                else:
                    stack.append([prices[i], i])
                    break
    
    for i in range(len(stack)):
        index = stack[i][1]
        answer[index] = len(answer) - index - 1

    return answer

print(solution([1, 2, 3, 2, 3]))

## GPT

from collections import deque

def solution(prices):
    stack = deque()
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            index = stack.pop()
            answer[index] = i - index
        stack.append(i)

    while stack:
        index = stack.pop()
        answer[index] = len(prices) - index - 1

    return answer

print(solution([1, 2, 3, 2, 3]))  # [4, 3, 1, 1, 0]