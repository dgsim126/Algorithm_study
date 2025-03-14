def solution(name, yearning, photo):
    dic= {}
    result= []

    for i in zip(name, yearning):
        dic[i[0]]= i[1]

    for i in range(len(photo)):
        sum_= 0
        for j in range(len(photo[i])):
            if(photo[i][j] in dic):
                sum_+=dic[photo[i][j]]
        result.append(sum_)

    return result

## main ##
name= ["may", "kein", "kain", "radi"]
yearning= [5, 10, 1, 3]
photo= [["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name, yearning, photo))