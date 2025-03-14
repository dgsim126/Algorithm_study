def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        if len(str(bin(arr1[i]))[2:]) < n:
            arr1[i] = '0'*(n-len(str(bin(arr1[i]))[2:])) + str(bin(arr1[i]))[2:]
        else:
            arr1[i] = str(bin(arr1[i]))[2:]
        if len(str(bin(arr2[i]))) < n:
            arr2[i] = '0'*(n-len(str(bin(arr2[i]))[2:])) + str(bin(arr2[i]))[2:]
        else:
            arr2[i] = str(bin(arr2[i]))[2:]

    for i in range(n):
        a = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                a = a + "#"
            else:
                a = a + " " 
        answer.append(a)
    return answer


print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))


print(bin(9))