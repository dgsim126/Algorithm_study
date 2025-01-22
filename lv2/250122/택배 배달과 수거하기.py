def solution(cap, n, deliveries, pickups):
    # 가장 먼 집부터 처리
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    answer = 0 # 총 이동거리
    d = 0 # 배달해야 하는 상자 누적
    p = 0 # 수거해야 하는 상자 누적

    for i in range(n):
        d += deliveries[i]
        p += pickups[i]

        # 배달, 수거 작업 처리 (0 될 때까지)
        while d > 0 or p > 0:
            d -= cap
            p -= cap
            answer += (n - i) * 2 # i 번째 집까지 거리 * 2 (왕복)

    return answer