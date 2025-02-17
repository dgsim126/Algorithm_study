# gpt
def solution(clothes):
    clothes_dict = {}

    # 1. 의상의 종류별 개수를 저장
    for _, kind in clothes:
        if kind in clothes_dict:
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1

    # 2. 모든 경우의 수 계산 (각 의상의 개수 + 1을 곱함)
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)  # 해당 종류의 의상을 선택하는 경우 + 선택하지 않는 경우

    return answer - 1  # 모든 의상을 안 입는 경우(1가지) 제외
