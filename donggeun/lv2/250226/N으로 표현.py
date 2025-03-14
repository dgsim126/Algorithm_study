'''
최소로 N을 활용해서 number를 만드는 경우는?
이걸 어떻게 풀어
'''


def solution(N, number):
    if N == number:
        return 1  # N이 number와 같다면 바로 1 반환

    dp = [set() for _ in range(9)]  # dp[i]: N을 i번 사용하여 만들 수 있는 숫자들
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))  # N을 i번 반복한 수 (예: 5, 55, 555)

    for i in range(1, 9):  # N 사용 횟수 (1~8번)
        for j in range(1, i):  # j와 i-j로 나누어 계산
            for num1 in dp[j]:
                for num2 in dp[i - j]:
                    dp[i].add(num1 + num2)  # 덧셈
                    dp[i].add(num1 - num2)  # 뺄셈
                    dp[i].add(num1 * num2)  # 곱셈
                    if num2 != 0:  # 0으로 나누는 경우 제외
                        dp[i].add(num1 // num2)  # 나눗셈 (정수 나눗셈)

        if number in dp[i]:  # 목표 숫자가 존재하면 반환
            return i

    return -1  # 8번 초과하면 -1 반환