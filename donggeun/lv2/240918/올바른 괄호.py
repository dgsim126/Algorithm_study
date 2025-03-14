def solution(s):
    stack= []

    for i in range(len(s)):
        stack.append(s[i])
        while(len(stack)>=2 and stack[-1]==")" and stack[-2]=="("):
            stack.pop()
            stack.pop()

    if(len(stack)>0):
        return False
    else:
        return True

## main ##
s= ")()("
print(solution(s))