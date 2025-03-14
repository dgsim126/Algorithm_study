def solution(s):
    num = 0

    for i in range(len(s)):
        if (s[i] == "("):
            num += 1
        else:
            num -= 1

        if (num < 0):
            return False

    if (num == 0):
        return True
    else:
        return False

