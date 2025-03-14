# gpt's help
def dfs(k, dungeons, visited, count):
    global max_count
    max_count = max(max_count, count)  # 최대 탐험 횟수 갱신

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], dungeons, visited, count + 1)  # 소모 피로도 차감 후 재귀 호출
            visited[i] = False


def solution(k, dungeons):
    global max_count
    max_count = 0
    visited = [False] * len(dungeons)  # 던전 방문 여부
    dfs(k, dungeons, visited, 0)
    return max_count


## main ##
k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))  # 출력: 3
