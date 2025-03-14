# def solution(want, number, discount):    
#     total = sum(number)
#     slice = discount[0:total]
#     dic = {want[i]: number[i] for i in range(len(want))}
#     for i in slice:
#         if dic[i] > 0:
#             dic[i] -= 1
#         if sum(dic.values()) > 0

    
#     while True:
        


# want = ["banana", "apple", "rice", "pork", "pot"]
# number = [3, 2, 2, 2, 1]
# discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
# print(solution(want, number, discount))

# GPT
from collections import Counter

def solution(want, number, discount):
    # 정현이가 원하는 제품과 수량을 딕셔너리로 변환
    want_dict = {w: n for w, n in zip(want, number)}
    
    # 10일 동안의 제품 목록을 카운트
    current_window = Counter(discount[:10])
    
    # 원하는 제품 조건과 일치하는 날짜 수
    result = 0
    
    # 전체 할인 리스트를 슬라이딩 윈도우로 탐색
    for i in range(len(discount) - 9):  # 10일씩 검사이므로 -9
        if all(current_window.get(product, 0) >= want_dict[product] for product in want_dict):
            result += 1
        
        # 윈도우를 슬라이딩
        if i + 10 < len(discount):  # 다음 슬라이딩 범위가 유효할 경우
            current_window[discount[i]] -= 1
            if current_window[discount[i]] == 0:
                del current_window[discount[i]]  # 값이 0이 되면 제거
            
            current_window[discount[i + 10]] += 1
    
    return result