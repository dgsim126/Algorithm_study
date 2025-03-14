def solution(survey, choices):
    answer = ''
    dic = {
        "A" : 0,
        "N" : 0,
        "C" : 0,
        "F" : 0,
        "M" : 0,
        "J" : 0,
        "R" : 0,
        "T" : 0
    }
    for i in range(len(survey)):
        if choices[i] > 4:
            dic[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            dic[survey[i][0]] += 4 - choices[i]
        else:
            continue

# GPT 삼항연산자

    first = "R" if dic["R"] >= dic["T"] else "T"
    second = "C" if dic["C"] >= dic["F"] else "F"
    third = "J" if dic["J"] >= dic["M"] else "M"
    fourth = "A" if dic["A"] >= dic["N"] else "N"

    answer = first + second + third + fourth

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))
print(solution(["RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA"],[4, 4, 4, 4, 4, 4, 4, 4]))
print(solution(["RT", "FC", "MJ", "AN", "TR", "CF", "JM", "NA"],[5, 3, 7, 2, 6, 1, 5, 3]))