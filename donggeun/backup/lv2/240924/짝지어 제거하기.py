def solution(s):
    stack= ["trash", "garbage"]

    for i in range(len(s)):
        stack.append(s[i])
        while(stack[-1]==stack[-2]):
            stack.pop()
            stack.pop()


    if(len(stack)==2):
        return 1
    else:
        return 0


## main ##
s= "baabaa"
print(solution(s))