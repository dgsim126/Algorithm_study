'''
lost와 reserve를 이용해 current를 만듦
current를 돌다가 0을 마주치면 해당 인덱스 앞에서 가져오거나, 뒤에서 가져오게 코드 작성
'''
from collections import deque


def solution(n, lost, reserve):  # 전체 학생 수, 잃어버린 학생, 여벌 체육복 학생
    lost = deque(lost)
    reserve = deque(reserve)
    current = [1 for _ in range(n)]

    while (lost):
        temp = lost.popleft()
        current[temp - 1] -= 1

    while (reserve):
        temp = reserve.popleft()
        current[temp - 1] += 1
    print(current)

    for i in range(len(current)):
        if (current[i] == 0):
            if (i > 0 and current[i - 1] == 2):
                current[i - 1] = 1
                current[i] = 1
            elif (i < len(current) - 1 and current[i + 1] == 2):
                current[i + 1] = 1
                current[i] = 1

    print(current)
    result = 0

    for i in range(len(current)):
        if (current[i] == 1 or current[i] == 2):
            result += 1

    return result