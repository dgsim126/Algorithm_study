def solution(p):
    global answer
    answer = ""
    if p == "":
        return ""
    else:
        splitFunction(p)

    return answer

def splitFunction(string):
    global answer
    cutNum = 0
    index = 0
    for i in range(len(string)):
        if string[i] == "(":
            cutNum += 1
        else:
            cutNum -= 1
        if cutNum == 0:
            index = i
            break
    if len(string) == index+1:
        u = string[0:index+1]
        v = ""
    else:
        u, v = string[0:index+1], string[index+1:]
        print(u, v)
    if type(isCorrectString(u)) == bool:
        answer = answer + u
        v = splitFunction(v)
        return
    
    else:
        v = splitFunction(v)
        u = "(" + v + ")" + isCorrectString(u)
        print("U", u)
        answer = answer + u
        return 

def isCorrectString(string):
    stringNum = 0
    isCorrect = True
    for i in range(len(string)):
        if string[i] == "(":
            stringNum += 1
        else:
            stringNum -= 1
        if stringNum < 0:
            isCorrect = False
            break
    if isCorrect == False:
        reverseString = ""
        for i in range(1,len(string)-1):
            if string[i] == "(":
                reverseString = reverseString + ")"
            else:
                reverseString = reverseString + "("
        print("reverse:", reverseString)
        return reverseString
    else:
        return True

print(solution("()))((()"))