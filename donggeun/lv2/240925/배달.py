from heapq import heappop, heappush


def solution(N, road, K):
    answer = 0
    distance = [1e9] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance[1] = 0
    h = [(0, 1)]

    while h:
        dis, node = heappop(h)

        if distance[node] < dis:
            continue

        for next_node, next_dis in graph[node]:
            d = dis + next_dis
            if distance[next_node] > d:
                distance[next_node] = d
                heappush(h, (d, next_node))

    for d in distance[1:]:
        if d <= K:
            answer += 1

    return answer