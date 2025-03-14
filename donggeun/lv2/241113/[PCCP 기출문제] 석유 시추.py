# gpt's help(내 코드는 효율성 테스트 실패)
from collections import deque, defaultdict

def bfs(land, x, y, group_id, group_sizes):
    dx = [1, 0, -1, 0]  # 동, 남, 서, 북
    dy = [0, 1, 0, -1]  # 동, 남, 서, 북
    queue = deque()
    queue.append((x, y))
    land[x][y] = group_id  # 방문 표시 및 그룹 ID 할당
    oil_size = 1  # 현재 석유 덩어리 크기

    while queue:
        current_x, current_y = queue.popleft()

        for i in range(4):
            new_x = current_x + dx[i]
            new_y = current_y + dy[i]
            if 0 <= new_x < len(land) and 0 <= new_y < len(land[0]) and land[new_x][new_y] == 1:
                land[new_x][new_y] = group_id  # 그룹 ID 할당
                queue.append((new_x, new_y))
                oil_size += 1  # 석유 덩어리 크기 증가

    group_sizes[group_id] = oil_size  # 그룹 ID에 대한 크기 저장

def solution(land):
    len_y = len(land)  # 세로
    len_x = len(land[0])  # 가로
    group_id = 2  # 그룹 ID 시작 (1은 이미 사용 중이므로 2부터 시작)
    group_sizes = {}  # 그룹 ID별 크기 저장

    # 모든 석유 덩어리를 그룹화하고 크기 계산
    for i in range(len_y):
        for j in range(len_x):
            if land[i][j] == 1:  # 아직 방문하지 않은 석유 덩어리
                bfs(land, i, j, group_id, group_sizes)
                group_id += 1

    max_oil = 0

    # 각 열을 탐색하여 최대 석유량 계산
    for col in range(len_x):
        seen_groups = set()  # 해당 열에서 이미 본 그룹을 저장
        total_oil = 0

        for row in range(len_y):
            cell_group_id = land[row][col]
            if cell_group_id > 1 and cell_group_id not in seen_groups:  # 석유 덩어리이며 처음 보는 그룹일 때
                total_oil += group_sizes[cell_group_id]
                seen_groups.add(cell_group_id)  # 현재 그룹을 추가

        max_oil = max(max_oil, total_oil)

    return max_oil

# main
land = [[0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [1, 1, 0, 0, 0, 1, 1, 0],
        [1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1]]

print(solution(land))  # 출력: 9
