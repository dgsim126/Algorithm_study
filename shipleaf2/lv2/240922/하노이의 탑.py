def hanoi(n, start, end, temp, result):
    if n == 1:
        # 원판이 하나일 때는 바로 3번 end로 옮기기
        result.append([start, end])
    else:
        # n-1개의 원판을 중간 기둥으로 옮기기
        hanoi(n-1, start, temp, end, result)
        # 가장 큰 원판을 목적지 기둥으로 옮기기
        result.append([start, end])
        # n-1개의 원판을 다시 목적지 기둥으로 옮기기
        hanoi(n-1, temp, end, start, result)

def solution(n):
    result = []
    # 하노이 탑 시작: n개의 원판을 1번에서 3번으로 옮기기
    hanoi(n, 1, 3, 2, result)
    return result
