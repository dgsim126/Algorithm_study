def solution(s):
    answer = []
    for i in range(len(s)):
        check = False
        save = [-1]
        for j in range(i):
            if s[j] == s[i]:
                save.append(j)
                check = True
        if check:
            answer.append(i-max(save))
        else:
            answer.append(-1)

    return answer