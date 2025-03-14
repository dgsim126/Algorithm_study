def cal(diffs, times, limit, level):
    result = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            result += times[i]
        else:
            if i == 0:
                # 첫 번째 퍼즐의 경우 이전 퍼즐 시간이 없으므로 단순 계산
                result += times[i] * (diffs[i] - level + 1)
            else:
                # 나머지 퍼즐은 이전 퍼즐 시간 포함
                result += ((times[i] + times[i - 1]) * (diffs[i] - level)) + times[i]

        if result > limit:  # 제한 시간을 초과하면 0 반환
            return 0
    return 1  # 제한 시간 내에 해결 가능하면 1 반환

def solution(diffs, times, limit):
    level_front = 1
    level_last = max(diffs)

    # 이진 탐색으로 가능한 레벨 범위를 줄여나갑니다
    while level_last - level_front > 5:
        current_level = (level_front + level_last) // 2
        if cal(diffs, times, limit, current_level) == 1:
            level_last = current_level  # 가능한 경우 더 작은 범위를 탐색
        else:
            level_front = current_level + 1  # 불가능한 경우 더 큰 범위를 탐색

    # 가능한 범위에서 정답을 찾습니다
    for i in range(level_front, level_last + 1):
        if cal(diffs, times, limit, i) == 1:
            return i

    return -1  # 모든 레벨을 시도했으나 답을 찾지 못한 경우 (이론적으로 발생하지 않음)
