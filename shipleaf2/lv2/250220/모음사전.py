def solution(word):
    result = 0
    current = ""
    num_dic = {
        "A": 0,
        "E": 1,
        "I": 2,
        "O": 3,
        "U": 4
    }

    num_list = ["A", "E", "I", "O", "U"]

    while current != word:
        print(current)
        if len(current) < 5:
            current += "A"
        elif len(current) == 5:
            if current[-1] != "U":
                current = current[0:4] + num_list[num_dic[current[-1]] + 1]
            elif current[-1] == "U":
                index = 0
                for i in range(-2, -6, -1):
                    if current[i] != "U":
                        index = i + 5
                        break
                current = current[0:index] + num_list[num_dic[current[index]] + 1]

        result += 1
    
    return result

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))