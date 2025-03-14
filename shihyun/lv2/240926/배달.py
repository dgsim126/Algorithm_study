# gpt
import heapq

def solution(N, road, K):
    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    # 최단 시간을 저장할 리스트 (무한대로 초기화)
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0  # 1번 마을에서의 거리 초기화
    
    # 우선순위 큐 (힙큐)를 이용한 다익스트라 알고리즘
    pq = [(0, 1)]  # (현재 거리, 현재 마을)
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_dist > dist[current_node]:
            continue
        
        for next_node, time in graph[current_node]:
            distance = current_dist + time
            
            if distance < dist[next_node]:
                dist[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
    
    # K 이하로 배달이 가능한 마을의 수 계산
    return len([d for d in dist if d <= K])