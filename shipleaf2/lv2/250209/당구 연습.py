def solution(m, n, startX, startY, balls):
    answer = []
    def calDist(ball):
        if ball[0] == startX:
            if abs(0 - startX) <= abs(m - startX):
                return (2 * startX) ** 2 + (startY - ball[1]) ** 2
            if abs(0 - startX) > abs(m - startX):
                return (startX - (m + (m - ball[0]))) ** 2 + (startY - ball[1]) ** 2
        elif ball[1] == startY:
            if abs(0 - startY) <= abs(n - startY):
                return (2 * startY) ** 2 + (startX - ball[0]) ** 2
            if abs(0 - startY) > abs(n - startY):
                return (startY - (n + (n - ball[1]))) ** 2 + (startX - ball[0]) ** 2
        else:
            list = []
            list.append((ball[0]+startX) ** 2 + (ball[1] - startY) ** 2)
            list.append((ball[0]-startX) ** 2 + (ball[1] + startY) ** 2)
            list.append((ball[0]-((m-startX)+m)) ** 2 + (ball[1] - startY) ** 2)
            list.append((ball[0]-startX) ** 2 + (ball[1] - ((n-startY)+n)) ** 2)
            return min(list)

    for ball in balls:
        answer.append(calDist(ball))

    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))

