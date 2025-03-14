# gpt's help
def solution(n, stages):  # 5, [2, 1, 2, 6, 2, 4, 3, 3]
    arrived = [0] * (n + 1)

    for stage in stages:
        if stage <= n:
            arrived[stage - 1] += 1  # 해당 스테이지에 도달한 사람 카운팅
        arrived[n] += 1  # 모든 스테이지를 클리어한 사람도 도달한 것으로 계산

    total_players = len(stages)  # 총 플레이어 수
    failure_rates = []

    for i in range(n):
        if total_players > 0:  # 해당 스테이지에 도달한 사람이 있는 경우
            failure_rate = arrived[i] / total_players
            total_players -= arrived[i]  # 다음 스테이지로 넘어갈 사람을 제외
        else:
            failure_rate = 0  # 도달한 사람이 없으면 실패율 0
        failure_rates.append((i + 1, failure_rate))  # (스테이지 번호, 실패율) 저장

    return mySort(failure_rates)

def mySort(arr):
    arr = sorted(arr, key=lambda x: (-x[1], x[0]))  # 실패율을 기준으로 내림차순 정렬
    return [stage for stage, rate in arr]  # 스테이지 번호만 반환

## main ##
n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))
