def solution(answers):
    num_one = [1,2,3,4,5]
    num_two = [2,1,2,3,2,4,2,5]
    num_three = [3,3,1,1,2,2,4,4,5,5]

    score_one = 0
    score_two = 0
    score_three = 0

    for i in range(len(answers)):
        if answers[i] == num_one[i % 5]:
            score_one += 1
        if answers[i] == num_two[i % 8]:
            score_two += 1
        if answers[i] == num_three[i % 10]:
            score_three += 1
    
    result = [score_one, score_two, score_three]

    highest = max(result)

    answer = []
    for i in range(len(result)):
        if result[i] == highest:
            answer.append(i+1)

    return answer

print(solution([1,2,3,4,5]))