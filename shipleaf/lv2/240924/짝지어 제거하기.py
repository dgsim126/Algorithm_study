# 시간초과 케이스를 제외하고 성공

# def solution(s):
#     index = 0
#     while len(s) != 0:
#         if index == len(s) - 1:
#             return 0
#         if s[index] == s[index+1]:
#             s = s[0:index] + s[index+2:]
#             index = 0
#         else:
#             index += 1
#     return 1

# # 테스트
# print(solution("baabaa"))
# print(solution("cdcd"))


# def solution(s):
#     list = []
#     for i in range(len(s)):
#         list.append(s[i])
#     index = 0
#     while len(list) != 0:
#         if index == len(s) - 1:
#             return 0
#         if list[index] == list[index+1]:
#             list.pop(index)
#             list.pop(index)
#             index = 0
#         else:
#             index += 1
#     return 1


# print(solution("baabaa"))
# print(solution("cdcd"))

def solution(s):
    stack = []
    
    for char in s:
        # 스택의 마지막 문자와 현재 문자가 같다면 제거
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    # 스택이 비어 있으면 모두 제거한 것이므로 1, 아니면 0 반환
    return 1 if not stack else 0

print(solution("baabaa"))
print(solution("cdcd"))