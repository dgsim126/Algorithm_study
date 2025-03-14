def solution(s):
    answer = []
    answer.append(-1) # 첫 번째 무조건

    for i in range(1, len(s)):
        n = 0
        if s[i] == s[i-1]: # 현재 값이 이전 값과 같다면
            answer.append(1)
        else: # 현재 값이 이전 값과 같지 않다면
            # 앞에 것들 중 가장 마지막에 있는 값을 찾아야 함
            for j in range(i, 0, -1): # 역순으로 도는 중
                n += 1
                if s[j-1] == s[i]:
                    answer.append(n)
                    break
                if n == i:
                    answer.append(-1)
    return answer

# # 테스트
print(solution("oaabaro"))