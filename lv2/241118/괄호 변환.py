# 친구들아 미안해..
# google
def check(s):
    stack = []

    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def divide(s):
    left, right = 0,0
    for i in range(len(s)):
        if s[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return s[:i+1], s[i+1:]

def solution(p):
    if not p:
        return ''

    u, v = divide(p)

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for s in u[1:len(u)-1]:
            if s == '(':
                answer += ')'
            else:
                answer += '('
        return answer