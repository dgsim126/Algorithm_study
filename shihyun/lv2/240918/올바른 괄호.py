def solution(s):
    answer = True
    save = []
    
    for i in s:
        if i == '(':
            save.append(i)
        elif i == ')':
            if save and save[-1] == '(':
                save.pop()
            else:
                answer = False
                break
    if save:
        answer = False

    return answer