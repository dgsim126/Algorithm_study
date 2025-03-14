def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1, len(s)):
        n = 0
        if s[i] == s[i-1]:
            answer.append(1)
        else:
            for j in range(i, 0, -1):
                n += 1
                if s[j-1] == s[i]:
                    answer.append(n)
                    break
                if n == i and s[0] != s[i]:
                    answer.append(-1)
                if n == i and s[0] == s[i]:
                    answer.append(n)
    return answer

# # 테스트
print(solution("oaabaro"))