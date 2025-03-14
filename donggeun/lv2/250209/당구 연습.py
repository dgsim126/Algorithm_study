# 어느 방향으로 원쿠션을 하는 것이 최적인지를 어떻게 찾아낼까? 공식?
# 그냥 4방향 모두 구한 후 가장 짧은 거리인 경우를 반환해야 하나?


def solve(x, y, startX, startY, ballX, ballY):
    dists = []
    # 위쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 크면 안된다.
    if not (ballX == startX and ballY > startY):
        d2 = (ballX - startX) ** 2 + (ballY - 2 * y + startY) ** 2
        dists.append(d2)
    # 아래쪽 벽
    # 단, x좌표가 같고 목표의 y가 더 작으면 안된다.
    if not (ballX == startX and ballY < startY):
        d2 = (ballX - startX) ** 2 + (ballY + startY) ** 2
        dists.append(d2)
    # 왼쪽 벽에 맞는 경우
    # 단, y좌표가 같고 목표의 x가 더 작으면 안된다.
    if not (ballY == startY and ballX < startX):
        d2 = (ballX + startX) ** 2 + (ballY - startY) ** 2
        dists.append(d2)
    # 오른쪽 벽
    # 단, y좌표가 같고 목표의 x가 더 크면 안된다.
    if not (ballY == startY and ballX > startX):
        d2 = (ballX - 2 * x + startX) ** 2 + (ballY - startY) ** 2
        dists.append(d2)

    return min(dists)


def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        answer.append(solve(m, n, startX, startY, ballX, ballY))
    return answer



## main ##
m= 10
n= 10
startX= 3
startY= 7
balls= [[7, 7], [2, 7], [7, 3]]
print(solution(m, n, startX, startY, balls))