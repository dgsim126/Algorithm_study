# gpt's help
def solution(n):
    answer = []

    def hanoi(n, start, stopover, dest):
        if n == 1:
            answer.append([start, dest])
            return

        hanoi(n - 1, start, dest, stopover)  # 1번 단계: n-1개의 원판을 경유지로 이동
        answer.append([start, dest])         # 2번 단계: 가장 큰 원판을 목적지로 이동
        hanoi(n - 1, stopover, start, dest)  # 3번 단계: 경유지에 있는 n-1개의 원판을 목적지로 이동

    hanoi(n, 1, 2, 3)  # 1: 출발지, 2: 경유지, 3: 목적지
    return answer

## main ##
n = 3
print(solution(n))
