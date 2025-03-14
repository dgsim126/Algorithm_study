from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     # bridge_length 길이 만큼의 queue를 생성하고 0으로 초기화
#     # queue에 값을 넣고 시간 1 증가
#
#     queue= [0]*bridge_length
#     truck_weights= deque(truck_weights)
#     time= 0
#
#     while(True):
#         # 탈출조건
#         if(len(truck_weights)==0 and sum(queue)==0):
#             print(sum(queue))
#             return time
#
#         if(len(truck_weights)>0 and sum(queue[1:bridge_length+1])+truck_weights[0]<=weight):
#             temp= truck_weights.popleft()
#             queue= queue[1:bridge_length+1]
#             queue.append(temp)
#             time+=1
#         else:
#             queue = queue[1:bridge_length + 1]
#             queue.append(0)
#             time+=1
#
#         # print(time, queue)

from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    truck_weights = deque(truck_weights)
    time = 0
    current_weight = 0  # 다리 위에 있는 트럭의 총 무게를 추적하는 변수

    while True:
        if len(truck_weights) == 0 and current_weight == 0:
            return time

        # 다리에서 트럭을 내린다
        leaving_truck = queue.pop(0)
        current_weight -= leaving_truck

        # 새 트럭이 다리로 들어갈 수 있는지 확인
        if len(truck_weights) > 0 and current_weight + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            queue.append(new_truck)
            current_weight += new_truck
        else:
            queue.append(0)

        time += 1

## main ##
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))


## main ##
bridge_length= 2
weight= 10
truck_weights= 	[7,4,5,6]
print(solution(bridge_length, weight, truck_weights))