# all gpt
import math

def solution(n, k):
    numbers = list(range(1, n + 1))  # 1부터 n까지의 숫자 리스트
    answer = []

    k -= 1  # 0-based index로 맞추기 위해 k를 1 줄임

    # 각 자리의 숫자를 결정
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)  # 남은 숫자들의 경우의 수 (i-1)!
        index = k // fact  # k가 속한 그룹의 인덱스 계산
        answer.append(numbers.pop(index))  # 해당 인덱스에 해당하는 숫자를 선택
        k %= fact  # k를 업데이트하여 다음 자리 결정

    return answer


# main
n = 3
k = 5
print(solution(n, k))
