import heapq


def solution(n, k, enemy):
    max_heap = []  # 최대 힙으로 사용
    total = 0  # 현재까지의 병력 소모량

    for i in range(len(enemy)):
        heapq.heappush(max_heap, -enemy[i])  # 적의 수를 최대 힙에 저장
        total += enemy[i]  # 병력 소모량에 추가

        # 현재 병력이 부족하면 무적권을 사용
        if total > n:
            if k > 0:
                # 가장 큰 적의 수를 무적권으로 처리
                total += heapq.heappop(max_heap)
                k -= 1
            else:
                # 무적권이 없으면 더 이상 진행 불가
                return i
## main ##
n= 7 # 내 병사 수
k= 3 # 무적권(내 병사 소모 없이 해당 라운드 적 모두 제거 가능)
enemy= [4, 2, 4, 5, 3, 3, 1] # 라운드 별 적의 수
print(solution(n, k, enemy))