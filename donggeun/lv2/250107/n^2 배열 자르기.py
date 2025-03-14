# def solution(n, left, right): # 시간초과(2차원 배열 모두 계산한 후 슬라이싱 하기에 시간초과)
#     lst= []
#     start = 0
#     for i in range(n):
#         temp= [start+1] * (start+1)
#         for j in range(start+1, n):
#             temp.append(temp[-1]+1)
#         start+=1
#         lst.append(temp)
#
#     result= []
#     for i in range(len(lst)):
#         for j in range(len(lst[0])):
#             result.append(lst[i][j])
#
#     return result[left:right+1]

# gpt의 미친 아이디어
def solution(n, left, right):
    result = []
    for idx in range(left, right + 1):
        # 1차원 배열의 idx를 2차원 배열로 변환
        row = idx // n  # 행 번호
        col = idx % n   # 열 번호
        # 각 위치에서의 값 계산
        result.append(max(row, col) + 1)
    return result


## main ##
n= 3
left= 2
right= 5
print(solution(n, left, right))