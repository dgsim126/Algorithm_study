# 시간 초과
def solution(numbers):
    n = len(numbers)
    answer = [-1]*n

    for i in range(n):
        for j in range(i + 1, n):
            if numbers[j] > numbers[i]:
                answer[i] = numbers[j]
                break

    return answer

def solution(numbers):
    n = len(numbers)
    answer = [-1]*n
    stack = []

    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]

        stack.append(i)

    return answer