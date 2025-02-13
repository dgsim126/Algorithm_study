def solution(plans):
    answer = []
    plans = plans
    for plan in plans:
        plan[1] = int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1])
        plan[2] = int(plan[2])
    sorted_plan = sorted(plans, key=lambda x: x[1])
    start_time, end_time = sorted_plan[0][1], sorted_plan[-1][1]
    stack = []
    current_name, start, playtime = sorted_plan.pop(0)
    playtime += 1
    for time in range(start_time, end_time + 1):
        playtime -= 1
        if sorted_plan[0][1] == time:
            if playtime == 0:
                answer.append(current_name)
            else:
                stack.append([current_name, start, playtime])
            current_name, start, playtime = sorted_plan.pop(0)
        else:
            if stack:
                if playtime == 0:
                    answer.append(current_name)
                    current_name, start, playtime = stack.pop(-1)
            else:
                if playtime == 0:
                    answer.append(current_name)
                    current_name, start, playtime = stack.pop(-1)
        
        if time == end_time:
            answer.append(current_name)
        
    if stack:
        for i in range(-len(stack)):
            answer.append(stack[0])

    return answer


# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))


# def solution(plans):
#     answer = []
#     # 시간 변환 및 정렬
#     for plan in plans:
#         plan[1] = int(plan[1].split(":")[0]) * 60 + int(plan[1].split(":")[1])
#         plan[2] = int(plan[2])

#     sorted_plans = sorted(plans, key=lambda x: x[1])  # 시작 시간 기준 정렬
#     stack = []

#     while sorted_plans:
#         current_name, start_time, duration = sorted_plans.pop(0)
        
#         # 다음 과제가 있는 경우
#         if sorted_plans:
#             next_start = sorted_plans[0][1]

#             # 현재 과제가 끝나는 시간
#             end_time = start_time + duration

#             if end_time > next_start:
#                 # 현재 과제가 끝나지 않았는데 다음 과제가 시작하면 남은 부분을 스택에 저장
#                 stack.append([current_name, end_time - next_start])
#             else:
#                 # 현재 과제가 끝났다면 정답에 추가
#                 answer.append(current_name)

#                 # 끝난 후에도 시간이 남아 있으면 스택에 저장된 과제 수행
#                 remaining_time = next_start - end_time
#                 while remaining_time > 0 and stack:
#                     prev_name, prev_duration = stack.pop()
#                     if prev_duration <= remaining_time:
#                         answer.append(prev_name)
#                         remaining_time -= prev_duration
#                     else:
#                         stack.append([prev_name, prev_duration - remaining_time])
#                         break
#         else:
#             # 마지막 과제는 무조건 끝낼 수 있음
#             answer.append(current_name)

#     # 스택에 남아 있는 과제 순서대로 처리
#     while stack:
#         answer.append(stack.pop()[0])

#     return answer

# # 테스트
# print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
# print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]))