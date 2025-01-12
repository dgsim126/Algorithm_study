def solution(elements):
    n = len(elements)
    extended = elements * 2  # 원형 수열처럼 다루기 위해 두 번 이어붙임
    unique_sums = set()  # 중복 제거를 위한 집합

    # 부분 수열 길이를 1부터 n까지 순회
    for length in range(1, n + 1):
        # 슬라이딩 윈도우를 사용하여 합 계산
        for start in range(n):  # 시작점은 0부터 n-1까지
            current_sum = sum(extended[start:start + length])
            unique_sums.add(current_sum)
    
    return len(unique_sums)
