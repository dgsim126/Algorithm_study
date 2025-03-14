# def solution(numbers):
#     answer = []
#     numbers_list = list(set(numbers))
#     numbers_list.append(0)
#     next_num = {}
#     for i in range(len(numbers_list)-1):
#         next_num[numbers_list[i]] = numbers_list[i+1]
#     print(next_num)
#     for i in numbers:
#         if next_num[i] == 0:
#             answer.append(-1)
#         else:
#             answer.append(next_num[i])

#     return answer

## 당연히 시간초과
# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         num = 0
#         for j in range(i+1, len(numbers)):
#             if numbers[j] > numbers[i]:
#                 num = numbers[j]
#                 break
#             else:
#                 continue
#         if num != 0:
#             answer.append(num)
#         else:
#             answer.append(-1)
#     return answer

## GPT
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers) - 1, -1, -1):
        while stack and stack[-1] <= numbers[i]:
            stack.pop()

        if stack:
            answer[i] = stack[-1]

        stack.append(numbers[i])

    return answer

print(solution([9, 1, 5, 3, 6, 2]))