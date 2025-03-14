# 테스트 케이스 3번 실패(87.5%)

def solution(n, arr1, arr2):
    sol1 = toTwo(arr1, n)
    sol2 = toTwo(arr2, n)
    result= [""]*n

    print(sol1)
    print(sol2)

    for i in range(n):
        for j in range(n):
            if(sol1[i][j]==1 or sol2[i][j]==1):
                result[i]+="#"
            else:
                result[i]+=" "

    return result


def toTwo(arr, n):
    result = [[0 for i in range(n)] for j in range(n)]  # 2차원 배열 만들기

    for i in range(len(arr)):
        binary = bin(arr[i])[2:]  # 2진수 변환
        binary = binary.zfill(n)  # n 자리에 맞춰서 앞에 0 채우기

        for j in range(n):
            result[i][j] = int(binary[j])  # 각 자리를 배열에 넣기

    print(result)


## main ##
n = 5
arr1 = 	[9, 20, 28, 18, 11]
arr2 = 	[30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))