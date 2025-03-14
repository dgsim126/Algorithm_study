def solution(survey, choices):
    dic = {
        "R": 0,
        "T": 0,
        "C": 0,
        "F": 0,
        "J": 0,
        "M": 0,
        "A": 0,
        "N": 0
    }

    # 점수 계산 로직
    for i in range(len(survey)):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3

    result = ""
    result += "R" if dic["R"] >= dic["T"] else "T"
    result += "C" if dic["C"] >= dic["F"] else "F"
    result += "J" if dic["J"] >= dic["M"] else "M"
    result += "A" if dic["A"] >= dic["N"] else "N"

    return result

# main
survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
print(solution(survey, choices))  # 출력: "TCMA"
