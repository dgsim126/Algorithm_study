def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = [0] * bridge_length
    weight_sum = 0

    while bridge:
        time += 1

        weight_sum -= bridge.pop(0)

        if truck_weights:
            if weight_sum + truck_weights[0] <= weight: # 다리에 추가로 올라갈 수 있으면
                new_truck = truck_weights.pop(0)
                bridge.append(new_truck)
                weight_sum += new_truck

            else:
                bridge.append(0)

    return time