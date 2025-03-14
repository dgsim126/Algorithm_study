# google's help
# 거꾸로 2를 나눠가면서 구할 것. 2로 안 나눠지는 경우 점프가 필요한 것이므로 건전지 사용 +1
def solution(N):
    answer = 0
    while N > 0:
        answer += N % 2
        N //= 2
    return answer

## main ##
N= 5
print(solution(N))