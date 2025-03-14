# 하나씩 탐색하는건 복잡도 문제 우려
# 어차피 2인 제한인건 같으니, 내림차순 정렬해서 덩치, 멸치 세트로 나가면 최선 아닌가?

from collections import deque

def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    required = 0

    while people:
        required += 1
        if len(people) == 1:
            break

        if people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
            
    return required

print(solution([70, 50, 80, 50], 100))