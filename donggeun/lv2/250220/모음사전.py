def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]  # 각 자리의 가중치
    result = 0

    for i, char in enumerate(word):
        index = vowels.index(char)  # 현재 문자의 인덱스 (0부터 시작)
        result += index * weights[i] + 1  # 현재 문자 기준으로 가중치를 적용한 값 추가

    return result
