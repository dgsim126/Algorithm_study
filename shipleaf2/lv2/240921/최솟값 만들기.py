def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i] * B[-(i+1)]
    return answer

# 테스트
print(solution([1, 4, 2], [5, 4, 4]))