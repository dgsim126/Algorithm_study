def solution(str1, str2):
    str1= str1.upper()
    str2= str2.upper()
    dic_= {}

    for i in range(1, len(str1)):
        if(str1[i-1].isalpha() and str1[i].isalpha()):
            dic_[str1[i-1:i+1]]= 1

    for i in range(1, len(str2)):
        if (str2[i-1].isalpha() and str2[i].isalpha()):
            if str2[i-1:i+1] in dic_:
                dic_[str2[i-1:i+1]]+= 1
            else:
                dic_[str2[i-1:i+1]]= 1
    print(dic_)


    ## 확률 구하기
    mom= len(dic_)
    son= 0
    for value in dic_.values():
        if(value!=1):
            son+=1

    if(son!=0 and mom!=0):
        return int(((son/mom)*65536))
    else:
        return 65536



## main ##
str1= "E=M*C^2"
str2= "e=m*c^2"
print(solution(str1, str2))