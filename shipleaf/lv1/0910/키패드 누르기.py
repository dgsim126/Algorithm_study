def solution(numbers, hand):
    answer = ''
    dic = {
        1 : ["L", [0, 3]],
        2 : ["C", [1, 3]],
        3 : ["R", [2, 3]],
        4 : ["L", [0, 2]],
        5 : ["C", [1, 2]],
        6 : ["R", [2, 2]],
        7 : ["L", [0, 1]],
        8 : ["C", [1, 1]],
        9 : ["R", [2, 1]],
        0 : ["C", [1, 0]],
    }
    loc = {
        "left" : [0, 0],
        "right" : [2, 0]
    }
    for i in numbers:
        to_left = abs(dic[i][1][0]-loc["left"][0]) + abs(dic[i][1][1]-loc["left"][1])
        to_right = abs(dic[i][1][0]-loc["right"][0]) + abs(dic[i][1][1]-loc["right"][1])
        if dic[i][0] == "L":
            answer += "L"
            loc["left"] = dic[i][1]
        elif dic[i][0] == "R":
            answer += "R"
            loc["right"] = dic[i][1]
        else:
            if to_left < to_right:
                answer += "L"
                loc["left"] = dic[i][1]
            elif to_left > to_right:
                answer += "R"
                loc["right"] = dic[i][1]
            else:
                if hand == "right":
                    answer += "R"
                    loc["right"] = dic[i][1]
                else:
                    answer += "L"
                    loc["left"] = dic[i][1]
        print(answer)

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))