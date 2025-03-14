# def solution(scoville, K):
#     cnt= 0
#
#     while(min(scoville)<K):
#         first= scoville.pop(scoville.index(min(scoville)))
#         second= scoville.pop(scoville.index(min(scoville)))
#         new_taste= first+(second*2)
#         scoville.append(new_taste)
#         cnt+=1
#
#     return cnt

import heapq

def solution(scoville, K):
    # 최소 힙 생성
    heapq.heapify(scoville)
    mix_count = 0

    while scoville[0] < K:
        # 더 이상 섞을 수 없는 경우 -1 반환
        if len(scoville) < 2:
            return -1

        # 스코빌 지수가 가장 낮은 두 개의 음식을 꺼내 섞는다
        least_spicy = heapq.heappop(scoville)
        second_least_spicy = heapq.heappop(scoville)
        new_scoville = least_spicy + (second_least_spicy * 2)

        # 새로 섞은 음식의 스코빌 지수를 힙에 추가
        heapq.heappush(scoville, new_scoville)
        mix_count += 1

    return mix_count



## main ##
scoville= [1, 2, 3, 9, 10, 12]
K= 7
print(solution(scoville, K))