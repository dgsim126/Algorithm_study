def solution(priorities, location):
    answer = 0
    dic = {}
    for i in range(priorities):
        if priorities[i] not in dic:
            dic[priorities[i]] = [i]
        else:
            dic[priorities[i]].append(i)
    for i in dic.keys():
        if i > priorities[location]:
            answer += len(dic[priorities[location]])
        elif i == priorities[location]:
            for j in len(dic[i]):
                if j > 
    return answer