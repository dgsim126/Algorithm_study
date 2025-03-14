# 운영체제 시간에 배운 것 같은데....

def solution(plans):
    # 시간을 분 단위로 변환하는 함수
    def time_to_minutes(time_str):
        hh, mm = map(int, time_str.split(":"))
        return hh * 60 + mm  # 전체 분 단위 변환

    # 과제 리스트를 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: time_to_minutes(x[1]))

    result = []  # 과제를 끝낸 순서 저장
    stack = []  # 멈춘 과제 저장
    current_time = 0  # 현재 시간

    for i in range(len(plans)):
        name, start, playtime = plans[i]
        start_time = time_to_minutes(start)
        playtime = int(playtime)

        # 현재 진행 중인 과제가 있다면, 새로운 과제 시작 전까지 시간 처리
        while stack and current_time < start_time:
            prev_name, remaining_time = stack.pop()

            # 남은 시간이 충분하면 현재 시간 업데이트 후 종료
            if current_time + remaining_time <= start_time:
                current_time += remaining_time
                result.append(prev_name)
            else:
                # 시간이 부족하면 남은 시간을 업데이트하고 다시 스택에 추가
                stack.append((prev_name, remaining_time - (start_time - current_time)))
                current_time = start_time
                break

        # 새로운 과제 시작
        current_time = start_time + playtime
        result.append(name)

        # 다음 과제가 있다면, 진행 중인 과제 스택에 저장
        if i < len(plans) - 1:
            next_start_time = time_to_minutes(plans[i + 1][1])
            if current_time > next_start_time:
                stack.append((name, current_time - next_start_time))
                result.pop()  # 아직 과제를 완료한 것이 아니므로 제거
                current_time = next_start_time

    # 스택에 남아 있는 과제 처리 (가장 최근에 멈춘 과제부터 실행)
    while stack:
        result.append(stack.pop()[0])

    return result
