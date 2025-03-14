# 가장 먼저 머릿속에 떠오르는 해결 방법은 wires를 순서대로 하나씩 제거해본 후 두 전력망의 차이를 저장하는 것.
# 즉, wires 리스트에서 하나씩 제거해본 후 전력망 차이의 최솟값을 구하면 됨.
# 더 효율적인 방법이 있을까??
# 문제 분야가 완전탐색인 것을 보아 맞을 것 같음
from copy import deepcopy


# 1. 일단 wires에서 하나를 제거
# 2. dfs를 사용해서 노드 수 계산(한쪽 전력망)
# 3. 총 노드 수에서 방금 구한 값을 빼면 반대쪽 전력망을 구할 수 있음
# 4. 두 차이 구하기

# gpt's help
def dfs(node, graph, visited):
    global cnt
    visited[node] = True
    cnt += 1

    # 연결된 노드 탐색
    for neighbor in graph[node]:
        if not visited[neighbor]:  # 방문하지 않은 노드만 탐색
            dfs(neighbor, graph, visited)

def solution(n, wires):
    min_difference = float('inf')

    for i in range(len(wires)):
        global cnt
        cnt = 0

        # 1. 그래프 생성
        graph = {i: [] for i in range(1, n + 1)}
        for j, (v1, v2) in enumerate(wires):
            if i == j:  # 현재 간선을 제거
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)

        # 2. 방문 여부 초기화
        visited = [False] * (n + 1)

        # 3. 한쪽 전력망의 노드 개수 계산
        dfs(1, graph, visited)
        sub_network_count = cnt
        other_network_count = n - sub_network_count

        # 4. 두 전력망의 차이 계산
        difference = abs(sub_network_count - other_network_count)
        min_difference = min(min_difference, difference)

    return min_difference

## main ##
n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
print(solution(n, wires))  # 출력: 3
