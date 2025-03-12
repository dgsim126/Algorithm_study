def solution(name, yearning, photo):
    answer = []
    dic = {}

    for i in range(len(name)):
        dic[name[i]] = yearning[i] # chatgpt

    for people in photo:
        sum = 0
        for person in people:
            if person in dic:
                sum += dic[person]
        answer.append(sum)

    return answer