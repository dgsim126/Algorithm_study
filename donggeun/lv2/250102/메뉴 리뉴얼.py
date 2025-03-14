# gpt's help
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # 1. 각 단품 메뉴를 정렬
    orders = [''.join(sorted(order)) for order in orders]
    print(orders)

    # 2. course 배열에 따른 조합 생성 및 빈도 계산
    for size in course:
        combinations_list = []
        for order in orders:
            # 손님 주문에서 size 크기의 조합 생성
            combinations_list.extend(combinations(order, size))

        print(combinations_list) # [('X', 'Y'), ('X', 'Z'), ('Y', 'Z'), ('W', 'X'), ('W', 'Y'), ('X', 'Y'), ('A', 'W'), ('A', 'X'), ('W', 'X')]

        # 조합 빈도 계산
        count = Counter(combinations_list)
        print(count) # Counter({('X', 'Y'): 2, ('W', 'X'): 2, ('X', 'Z'): 1, ('Y', 'Z'): 1, ('W', 'Y'): 1, ('A', 'W'): 1, ('A', 'X'): 1})

        # 3. 최다 빈도 조합 찾기 (최소 2번 이상)
        if count:
            max_count = max(count.values())
            if max_count >= 2:
                # 최다 빈도 조합 필터링
                answer.extend([''.join(combo) for combo, freq in count.items() if freq == max_count])

    # 4. 결과를 사전순 정렬
    return sorted(answer)


# 테스트 코드
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))
