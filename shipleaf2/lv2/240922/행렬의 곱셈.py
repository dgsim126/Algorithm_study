# def solution(arr1, arr2):
#     # answer = [[[0] * len(arr2[0])] * len(arr1)]   # 얕은 참조 이슈 GPT
#     answer = [[[0] * len(arr2[0]) for _ in range(len(arr1))]]
#     print(answer)
#     # matrix_arr = [[[]] * len(arr2[0])] * len(arr1)
#     matrix_arr = [[[] for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
#     print(len(matrix_arr))
#     for i in range(len(arr1)):  # 첫 번째 행렬의 행 값 넣기
#         for j in range(len(arr2[0])):
#             print(i, j, arr1[i])
#             matrix_arr[i][j].append(arr1[i])
#     for i in range(len(arr2[0])):   # 두 번째 행렬의 열 값 넣기
#         column_matrix = []  
#         for j in range(len(arr2)):
#             column_matrix.append(arr2[j][i])
#         for k in range(len(matrix_arr)):
#             matrix_arr[k][i].append(column_matrix)
#     print(matrix_arr)
#     for i in range(len(answer)):
#         number = 1
#         for j in range(len(answer[0])):
#             for k in range(len(matrix_arr[0][0])):
#                 number = matrix_arr[i][j][k]

#     return answer

# def solution(arr1, arr2):
#     answer = [[]]
#     return answer

# list = []
# list.append([1,2,3])
# print(list)

# GPT

def solution(arr1, arr2):
    # arr1의 행(row) 수, arr2의 열(column) 수
    n = len(arr1)
    m = len(arr1[0])
    p = len(arr2[0])
    
    # 결과 행렬 초기화 (크기는 n x p)
    result = [[0] * p for _ in range(n)]
    
    # 행렬 곱셈 수행
    for i in range(n):
        for j in range(p):
            for k in range(m):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result

print(solution([[1, 4], [3, 2], [4, 1]],[[3, 3], [3, 3]]))