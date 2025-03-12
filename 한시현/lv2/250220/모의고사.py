def solution(answers):
    no1 = [1, 2, 3, 4, 5]
    no2 = [2, 1, 2, 3, 2, 4, 2, 5]
    no3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]

    for i in range(len(answers)):
        if answers[i] == no1[i % len(no1)]:
            count[0] += 1
        if answers[i] == no2[i % len(no2)]:
            count[1] += 1
        if answers[i] == no3[i % len(no3)]:
            count[2] += 1

    max_score = max(count)

    answer = []
    for j in range(len(count)):
        if max_score == count[j]:
            answer.append(j+1)

    return answer