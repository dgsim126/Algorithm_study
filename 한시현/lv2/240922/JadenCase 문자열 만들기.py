def solution(s):
    s = s.lower()
    s = list(s)
    if s[0] not in ['0','1','2','3','4','5','6','7','8','9']:
        s[0] = s[0].upper()
    
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            s[i] = s[i].upper()

    answer = ''.join(s)  # join()

    return answer

# def solution(s):
#     s = s.lower()
#     text = list(map(str, s.split()))
#     answer = ''
#     for word in text:
#         if word[0] not in ['0','1','2','3','4','5','6','7','8','9']:
#             wordlist = list(word) # 문자열은 불변 타입
#             wordlist[0] = wordlist[0].upper()
#             answer += ''.join(wordlist) + ' '
#         else:
#             answer += word + ' '
            
#     return answer[:len(answer)-1]