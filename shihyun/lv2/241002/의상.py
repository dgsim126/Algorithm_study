# gpt
def solution(clothes):
    closet = {} # '키': ['값']

    for name, kind in clothes:
        if kind in closet.keys():
            closet[kind] += [name]  # 이미 해당 종류가 있으면 이름 추가
        else:
            closet[kind] = [name]  # 새로운 종류면 새 리스트로 추가
    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수는 (N+1)(M+1)
    answer = 1
    for _, value in closet.items():
        answer *= (len(value) + 1)  # 각 종류별로 (의상 수 + 1)
        
    return answer - 1  # 아무것도 입지 않는 경우 제외