def solution(A,B):
    A.sort()
    B.sort(reverse= True)
    result= 0

    for i in range(len(A)):
        result+=(A[i]*B[i])

    return result

## main ##
A= [1, 4, 2]
B= [5, 4, 4]
print(solution(A, B))
