def solution(s):
    answer = []
    s = s[2:len(s)-2]
    s = s.split('},{')
    if len(s) == 1:
        answer.append(int(s[0]))
    sorted_s = sorted(s, key=lambda x: len(x))
    for i in sorted_s:
        if len(sorted_s) >= 2:
            list = i.split(',')
            for j in list:
                if int(j) not in answer:
                    answer.append(int(j))
    return answer


# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{123}}"))
