def solution(answers):
    no1 = [1,2,3,4,5]
    no2 = [2,1,2,3,2,4,2,5]
    no3 = [3,3,1,1,2,2,4,4,5,5]
    count1 = 0
    count2 = 0
    count3 = 0

    for i in range(len(answers)):
        if answers[i] == no1[i % len(no1)]:
            count1 += 1
        if answers[i] == no2[i % len(no2)]:
            count2 += 1
        if answers[i] == no3[i % len(no3)]:
            count3 += 1
    
    check = max(count1, count2, count3)
    answer = []
    if check == count1:
        answer.append(1)
    if check == count2:
        answer.append(2)
    if check == count3:
        answer.append(3)

    return answer