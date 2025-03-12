# gpt
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]  # 자리별 가중치

    result = 0
    index = 0

    for char in word:
        result += vowels.index(char) * weights[index] + 1 # 단어 순서는 1부터 시작하므로 +1
        index += 1

    return result