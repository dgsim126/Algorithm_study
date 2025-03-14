# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0] * bridge_length
#     i = 0
#     while True:
#         if len(bridge) >= bridge_length:
#             bridge.pop(0)
#         if i > len(truck_weights) - 1:
#             answer += 2
#             break
#         if sum(bridge) + truck_weights[i] <= weight:
#             bridge.append(truck_weights[i])
#             i += 1
#         elif sum(bridge) + + truck_weights[i] > weight:
#             bridge.append(0)
#         print(bridge, answer)
#         answer += 1

#     return answer

# print(solution(2, 10, [7,4,5,6]))
# print(solution(100, 100, [10]))

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length # 다리를 표현한 list
    total_weight = 0
    i = 0 # 대기 트럭 index

    while bridge:
        answer += 1
        total_weight -= bridge.pop(0)  # 다리에서 맨 앞의 트럭을 이동시키고 무게를 줄임

        if i < len(truck_weights):  # 아직 대기 중인 트럭이 있다면
            if total_weight + truck_weights[i] <= weight:  # 새로운 트럭을 다리에 올릴 수 있으면
                bridge.append(truck_weights[i])  # 다리의 끝에 트럭을 추가
                total_weight += truck_weights[i]  # 다리 위 트럭 무게에 추가
                i += 1  # 대기 트럭 인덱스 증가
            else:
                bridge.append(0)  # 무게가 초과되면 빈 공간을 추가하여 트럭 이동을 유지

    return answer

# 예시 실행
print(solution(2, 10, [7, 4, 5, 6]))  # 출력: 8
print(solution(100, 100, [10]))  # 출력: 101
