def solution(dartResult):
    num = ['0','1','2','3','4','5','6','7','8','9','10']
    score = []

    for i in range(len(dartResult)):
        if dartResult[i] in num:
            if dartResult[i] == '1' and dartResult[i+1] == '0':
                score.append(10)
                continue
            if dartResult[i] == '0' and dartResult[i-1] == '1':
                continue
            score.append(int(dartResult[i]))

        elif dartResult[i] in ['S','D','T']:
            if dartResult[i] == 'S':
                score[-1] = score[-1] ** 1
            elif dartResult[i] == 'D':
                score[-1] = score[-1] ** 2
            elif dartResult[i] == 'T':
                score[-1] = score[-1] ** 3

        elif dartResult[i] in ['*','#']:
            if dartResult[i] == '*':
                score[-1] *= 2
                if len(score) > 1:
                    score[-2] *= 2
            elif dartResult[i] == '#':
                score[-1] *= -1
            
    return sum(score)