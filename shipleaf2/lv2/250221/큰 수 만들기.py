# 1. 전체 탐색 후 가장 큰 숫자가 되는 경우 뽑기 반복
# 2. 가장 앞 숫자끼리 비교 후 큰 배열로 반환 반복
# 3. for문 돌리면서 number[i] < number[i+1] 발견하면 pop하기(현재) + start index 업데이트
# 10번 케이스 시간 초과

# def solution(number, k):
#     num_list = list(number)
#     index = 0
#     while k > 0:
#         k -= 1
#         for i in range(index, len(num_list) - 1):
#             if num_list[i] < num_list[i+1]:
#                 num_list.pop(i)
#                 if i > 0:
#                     index = i - 1
#                 break
#             if i == len(num_list) - 2:
#                 for j in range(k+1):
#                     num_list.pop(-1)
#                     k = 0
#     return "".join(num_list)

# GPT

def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    return "".join(stack[:len(number)-k])  # 남은 k만큼 제거
                    
print(solution("1924", 2))