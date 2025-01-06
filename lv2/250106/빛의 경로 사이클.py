# GPT

def solution(grid):
    # 격자의 행과 열 크기
    rows, cols = len(grid), len(grid[0])
    
    # 방향 벡터: 위(0), 오른쪽(1), 아래(2), 왼쪽(3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # 방문 여부를 체크하는 3차원 배열 (x, y, 방향)
    visited = [[[False] * 4 for _ in range(cols)] for _ in range(rows)]
    
    def next_position(x, y, d):
        """현재 위치 (x, y)와 방향 d에서 이동 후의 위치와 방향을 계산."""
        nx, ny = (x + directions[d][0]) % rows, (y + directions[d][1]) % cols
        if nx < 0: nx += rows
        if ny < 0: ny += cols
        return nx, ny
    
    def change_direction(d, cell):
        """현재 방향 d와 칸의 유형 cell에 따라 새로운 방향을 반환."""
        if cell == 'S':
            return d
        elif cell == 'L':
            return (d - 1) % 4  # 좌회전
        elif cell == 'R':
            return (d + 1) % 4  # 우회전
    
    cycle_lengths = []  # 사이클 길이를 저장할 리스트
    
    # 모든 위치와 방향에 대해 순회
    for i in range(rows):
        for j in range(cols):
            for d in range(4):  # 방향 0~3
                if not visited[i][j][d]:  # 방문하지 않은 상태라면
                    x, y, direction = i, j, d
                    cycle_length = 0  # 현재 사이클의 길이
                    
                    while not visited[x][y][direction]:
                        visited[x][y][direction] = True  # 현재 위치와 방향 방문 체크
                        cycle_length += 1  # 사이클 길이 증가
                        
                        # 다음 위치와 방향 계산
                        direction = change_direction(direction, grid[x][y])
                        x, y = next_position(x, y, direction)
                    
                    # 사이클 길이를 저장
                    cycle_lengths.append(cycle_length)
    
    # 오름차순으로 정렬하여 반환
    return sorted(cycle_lengths)

# 테스트
print(solution(["SL", "LR"]))  # [16]
print(solution(["S"]))         # [1, 1, 1, 1]
print(solution(["R", "R"]))    # [4, 4]