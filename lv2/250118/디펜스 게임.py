import heapq

def solution(n, k, enemy):
    # 무적권 사용이 필요한 라운드에서의 적의 수를 저장할 최대 힙
    used_heap = []

    i = 0  # 라운드 인덱스
    while i < len(enemy):
        count = enemy[i] # 현재 라운드에서 적 수
        # 현재 라운드 적 수를 병사로 방어

        n -= count
        # 무적권 사용 기록을 힙에 저장 (음수로 저장해 최대 힙 구현)
        heapq.heappush(used_heap, -count)

        # 병사가 부족해진 경우
        if n < 0:
            # 무적권을 사용해야 한다
            if k > 0:
                # 가장 많은 병사를 소모했을 라운드를 무적권으로 대체
                n += -heapq.heappop(used_heap)
                k -= 1
            else:
                # 무적권도 없으면 게임 종료
                return i

        i += 1

    # 모든 라운드를 막을 수 있는 경우
    return len(enemy)