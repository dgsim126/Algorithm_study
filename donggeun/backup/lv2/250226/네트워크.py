'''
bfs? dfs?
각 모든 위치에서 시작하는 dfs라고 판단(네트워크의 최대 개수는 노드의 최대수보다 클 수 없기에)
모든 노드에서 dfs를 수행하고 이미 접근한 영역이라면 해당 점수를 2로 높이자!
그러면 0과 2가 아닌 1만 방문하면 된다.
탈출조건에 부딪힐 때가 아닌 다시 depth=0으로 복귀했을 때, cnt 증가. 최종결과로 return
코드 작성 시작
'''

# gpt
def solution(n, computers):
    def dfs(node):
        visited[node] = True  # 현재 노드 방문 체크
        for neighbor in range(n):  # 모든 노드 탐색
            if computers[node][neighbor] == 1 and not visited[neighbor]:  # 연결되어 있고 방문하지 않았다면
                dfs(neighbor)  # DFS 탐색

    visited = [False] * n  # 방문 여부 저장 리스트
    network_count = 0  # 네트워크 개수

    for i in range(n):  # 모든 노드를 탐색
        if not visited[i]:  # 방문하지 않은 노드라면 새로운 네트워크 시작
            dfs(i)
            network_count += 1  # 새로운 네트워크 발견

    return network_count


from collections import deque

def solution(n, computers):
    def bfs(start):
        queue = deque([start])
        visited[start] = True

        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if computers[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    visited = [False] * n
    network_count = 0

    for i in range(n):
        if not visited[i]:
            bfs(i)
            network_count += 1

    return network_count