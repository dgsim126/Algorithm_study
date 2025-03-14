def solution(n):
    fibonacci_arr = [0] * (n+1)
    fibonacci_arr[0] = 0
    fibonacci_arr[1] = 1

    for i in range(2, n+1):
        fibonacci_arr[i] = fibonacci_arr[i-1] + fibonacci_arr[i-2]

    return fibonacci_arr[n] % 1234567

# 테스트
print(solution(2))