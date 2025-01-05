# GPT

def solution(word):
    weights = [781, 156, 31, 6, 1]
    vowels = ['A', 'E', 'I', 'O', 'U']
    
    index = 0
    for i, char in enumerate(word):
        char_index = vowels.index(char)
        index += char_index * weights[i] + 1
    
    return index

print(solution("AAAAE"))
