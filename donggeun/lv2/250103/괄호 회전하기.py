def check(v):
    stack = []
    for char in v:
        if(char in "({["):
            stack.append(char)
        elif(char == ")" and (len(stack)==0 or stack[-1] != "(")):
            return 0
        elif(char == "}" and (len(stack)==0 or stack[-1] != "{")):
            return 0
        elif(char == "]" and (len(stack)==0 or stack[-1] != "[")):
            return 0
        else:
            stack.pop()

    if(len(stack)==0):
        return 1
    else:
        return 0

def solution(s):
    s= list(s)
    result= 0
    for _ in range(len(s)):
        if(check(s)==1):
            result+=1
        s.append(s.pop(0))
    return result

## main ##
s = "[](){}"
print(solution(s))
