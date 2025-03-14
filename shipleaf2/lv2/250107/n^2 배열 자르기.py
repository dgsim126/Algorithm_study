# def solution(n, left, right):
#     array = [[0 for i in range(n)] for j in range(n)]
#     array[0][0] = 1
#     for i in range(1, len(array)):
#         for j in range(0, i+1):
#             array[i][j] = i+1
#     for i in range(len(array)):
#         for j in range(1, len(array)):
#             array[i][j] = j+1
#     answer = array[0]
#     for i in range(1, len(array)):
#         answer += array[i]
#     print(array)
#     return answer[left:right+1]

def solution(n, left, right):
    array = [[1 for i in range(n)] for j in range(n)]
    for i in range(len(array)):
        for j in range(len(array)):
            if i == j:
                array[i][j] = i + 1
            elif i > j:
                array[i][j] = i + 1
            else:
                array[i][j] = j + 1
    answer = array[0]
    for i in range(1, len(array)):
        answer += array[i]
    # print(array)
    return answer[left:right+1]

print(solution(4,7,14))