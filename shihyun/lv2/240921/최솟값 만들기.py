def solution(A,B):
    sum = 0
    A.sort()
    B.sort()
    B.reverse()

    for i in range(len(A)):
        sum += A[i] * B[i]

    return sum