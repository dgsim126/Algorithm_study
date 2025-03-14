## 2. 음양 더하기

# def solution(absolute, signs):
#     answer = 0
#     for i in range(0, len(signs)):
#         if signs[i] == False:
#             answer = answer + (-1)*absolute[i]
#         else:
#             answer = answer + absolute[i]
#         print(answer)
#         print(absolute[i])
#     return answer

# a=list(map(int, input().split(',')))
# b=list(map(lambda x:x == 'true', input().split(',')))

# print(a,b)
# # print(solution(list(map(int, input().split(','))), list(map(bool, input().split(',')))))

# print(solution(a,b))