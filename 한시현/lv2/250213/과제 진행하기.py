def solution(plans):
    # 시간 변환 함수
    def time_to_minutes(time_str):
        h, m = map(int, time_str.split(":"))
        return h * 60 + m  # 시간을 분 단위로 변환

    # plans를 시작 시간을 기준으로 정렬
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    result = []  # 완료된 과제 목록
    stack = []   # 중단된 과제 저장
    current_time = 0  # 현재 시각

    for i in range(len(plans)):
        name, start_time, duration = plans[i]
        start_time = time_to_minutes(start_time)
        duration = int(duration)

        # 현재 진행 중인 과제 종료 처리 (중단된 과제 처리)
        while stack and current_time < start_time:
            prev_name, remaining_time = stack.pop()
            if current_time + remaining_time <= start_time:
                current_time += remaining_time
                result.append(prev_name)  # 완료된 과제 저장
            else:
                stack.append((prev_name, remaining_time - (start_time - current_time)))
                current_time = start_time
                break  # 새 과제 시작해야 하므로 종료

        # 새로운 과제 시작
        current_time = start_time + duration
        result.append(name)

        # 다음 과제가 남아있고, 현재 과제가 끝나기 전에 시작해야 한다면 스택에 저장
        if i < len(plans) - 1 and current_time > time_to_minutes(plans[i + 1][1]):
            stack.append((name, current_time - time_to_minutes(plans[i + 1][1])))
            result.pop()  # 현재 과제는 중단되었으므로 결과에서 삭제

    # 모든 과제를 다 처리한 후 스택에 남아 있는 과제 처리
    while stack:
        result.append(stack.pop()[0])

    return result
