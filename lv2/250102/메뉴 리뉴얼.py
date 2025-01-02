from itertools import combinations
from collections import Counter # (gpt) Counter : 빈도 계산 도구. 요소를 key, 요소의 등장 횟수를 value로 저장

def solution(orders, course):
    combs = []
    for order in orders:
        sorted_order = sorted(order) # 메뉴 정렬
        for size in course:
            combs += list(combinations(sorted_order, size)) # 코스별 모든 메뉴 조합 생성

    counter = Counter(combs)
    print(counter)
    # 출력 예시
    # Counter({('A', 'C'): 4, ('C', 'D'): 3, ('C', 'E'): 3, ('D', 'E'): 3, ('C', 'D', 'E'): 3, ('B', 'C'): 2, ...

    # counter의 value를 통해 코스별 최대 주문 수를 보유한 메뉴 찾자

    # 친구들아 미안해..


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])