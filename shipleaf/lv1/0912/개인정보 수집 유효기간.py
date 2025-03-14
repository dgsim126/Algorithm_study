def solution(today, terms, privacies):
    answer = []
    dic = {}
    print(today)
    for i in range(len(terms)):
        dic[terms[i].split()[0]] = terms[i].split()[1]
    for i in range(len(privacies)):
        if calc(privacies[i].split()[0], dic[privacies[i].split()[1]]) <= today:
            answer.append(i+1)
    return answer

def calc(day, plus):
    YYYY = int(day.split(".")[0])
    MM = int(day.split(".")[1])
    DD = int(day.split(".")[2])

    MM = MM + int(plus)
    if MM > 12:
        MM = MM -12
        YYYY = YYYY + 1
    if MM < 10:
        MM = "0" + str(MM)
    if DD < 10:
        DD = "0" + str(DD)

    return str(YYYY) + "." + str(MM) + "." + str(DD)

print(solution("2025.01.01",["A 10", "B 12", "C 3"],["2023.01.01 A", "2024.01.01 B", "2024.09.01 C"]))
