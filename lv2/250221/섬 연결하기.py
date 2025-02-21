# # cost가 저렴한 순서로 정렬 후 a -> b 가는 방법이 없으면 잇기

from collections import deque
from copy import deepcopy


def solution(n, costs):
    total_cost = 0
    costs = sorted(costs, key=lambda x: x[2])
    bridge = {}

    def findPath(a, b, bridge):
        path_bridge = bridge.copy()
        start = deque([a])
        visited = [False] * n

        while start:
            x = start.popleft()
            visited[x] = True

            if b in path_bridge[x]:
                return True

            for i in path_bridge[x]:
                if not visited[i] and i in bridge:
                    start.append(i)
            
        return False
    
    for cost in costs:
        if cost[0] not in bridge:
            bridge[cost[0]] = deque([cost[1]])
            if cost[1] not in bridge:
                bridge[cost[1]] = deque([cost[0]])
            else:
                bridge[cost[1]].append(cost[0])
            total_cost += cost[2]
        else:
            if findPath(cost[0], cost[1], bridge):
                continue
            elif not findPath(cost[0], cost[1], bridge):
                bridge[cost[0]].append(cost[1])
                if cost[1] in bridge:
                    bridge[cost[1]].append(cost[0])
                else:
                    bridge[cost[1]] = deque([cost[0]])
                total_cost += cost[2]

    return total_cost


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))