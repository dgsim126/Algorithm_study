def solution(s):
    answer = ''
    s = s.lower()
    answer += s[0].upper()
    for i in range(1, len(s)):
        if s[i-1] == " ":
            if s[i] != " ":
                answer += s[i].upper()
            else:
                answer += s[i]
                continue
        else:
            answer += s[i]
    return answer

# 테스트

print(solution("3people unFollowed me"))
print(solution("for the last week"))
