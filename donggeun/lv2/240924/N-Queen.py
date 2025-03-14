def solution(n):
    global cnt
    cnt = 0

    result = [-1] * n  # 각 행에 퀸이 놓인 열의 위치를 저장하는 배열

    dfs(0, result, n)

    return cnt


def dfs(depth, result, n):
    global cnt

    # 탈출 조건: 모든 퀸이 배치되면 카운트를 증가시킴
    if depth == n:
        cnt += 1
        return

    for i in range(n):
        if is_safe(depth, i, result):
            result[depth] = i  # 현재 행(depth)의 퀸을 i번째 열에 놓음
            dfs(depth + 1, result, n)  # 다음 행으로 이동
            result[depth] = -1  # 백트래킹, 퀸을 다른 위치에 놓기 위해 초기화


def is_safe(depth, col, result):
    # 현재 (depth, col)에 퀸을 놓을 수 있는지 확인
    for i in range(depth):
        # 같은 열에 퀸이 있는지 확인 (세로 공격)
        if result[i] == col:
            return False
        # 대각선 공격 방지 (행 차이와 열 차이가 같으면 대각선 상에 있음)
        if abs(result[i] - col) == abs(i - depth):
            return False
    return True


## main ##
n = 4
print(solution(n))
