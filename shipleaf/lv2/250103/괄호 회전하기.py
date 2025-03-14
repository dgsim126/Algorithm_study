def solution(s):
    x = s
    count = 0
    for _ in range(len(s)):
        x = x[1:] + x[0]
        if isItCorrect(x):
            count += 1
    return count

def isItCorrect(s):
    list = []
    dict = {"(": 1, "{": 2, "[": 3, ")": -1, "}": -2, "]": -3}
    if dict[s[0]] == -1:
        return False
    for i in s:
        if dict[i] < 0:
            if list == []:
                return False
            else:
                if list[-1] + dict[i] != 0:
                    return False
                else:
                    list.pop(-1)
        else:
            list.append(dict[i])

    if list == []:
        return True

print(solution("[](){}"))
print(solution("}]()[{"))