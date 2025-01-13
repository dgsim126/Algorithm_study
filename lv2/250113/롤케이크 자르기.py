def solution(topping):
    result= 0

    set_1= set()
    set_1.add(topping[0])
    set_2= set()
    dic_1= {}
    dic_2= {}

    dic_1[topping[0]]= 1
    for i in range(1, len(topping)):
        set_2.add(topping[i])
        if topping[i] in dic_2:
            dic_2[topping[i]]+=1
        else:
            dic_2[topping[i]]= 1

    # print(set_1, set_2, dic_1, dic_2) # {1} {1, 2, 3, 4} {0: 1} {2: 2, 1: 3, 3: 1, 4: 1}
    if(len(set_1)==len(set_2)):
        result+=1

    for i in range(1, len(topping)):
        dic_2[topping[i]]-=1
        if(dic_2[topping[i]]==0):
            set_2.remove(topping[i])

        if topping[i] in dic_1:
            dic_1[topping[i]]+=1
        else:
            dic_1[topping[i]]= 1
            set_1.add(topping[i])

        if(len(set_2)==len(set_1)):
            result+=1

    return result








## main ##
topping= [1, 2, 1, 3, 1, 4, 1, 2]
print(solution(topping))