from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([])
    while True:
        if not bridge:
            bridge.append(truck_weights.pop(0))
        else:
            