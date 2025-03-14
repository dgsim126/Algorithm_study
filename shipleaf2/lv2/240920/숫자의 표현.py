# GPT

def solution(n):
    count = 0
    
    # k는 1부터 연속된 수의 개수를 의미
    k = 1
    while k * (k - 1) // 2 < n:
        # n - k(k-1)/2가 k로 나누어 떨어져야 시작 숫자 x가 자연수임
        if (n - (k * (k - 1) // 2)) % k == 0:
            count += 1
        k += 1
    
    return count
