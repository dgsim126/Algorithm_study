'''
before에서 맨 앞 값을 조회한다.(pop하는 것이 아니라 조회만)
- 현재 in_bridge의 합과 before에서 꺼낸 값의 합이 weight을 초과한다면 0을 넣는다.
- 합이 weight을 초과하지 않는다면 before에서 조회한 값을 append하고, before.popleft한다.
- 위의 로직을 수행하고 in_bridge의 길이가 bridge_length를 초과했다면 popleft한다
'''

from collections import deque


def solution(bridge_length, weight, truck_weights):
    after = deque()
    before = deque(truck_weights)
    in_bridge = deque()
    for i in range(bridge_length):
        in_bridge.append(0)
    in_sum = 0
    time = 0

    while (before):
        temp = before[0]
        if ((temp + in_sum) - in_bridge[0] > weight):  # temp를 넣으면 안되는 경우
            in_bridge.append(0)

        else:  # temp를 넣어도 되는 경우
            before.popleft()
            in_bridge.append(temp)
            in_sum += temp

        # 다리 길이 초과 확인
        if (len(in_bridge) > bridge_length):
            temp = in_bridge.popleft()
            in_sum -= temp

        time += 1
        # print(f"{time}초: {in_bridge}")

    time += bridge_length
    return time




