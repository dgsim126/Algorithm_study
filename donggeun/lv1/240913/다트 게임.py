def solution(dartResult):
    temp= []
    lst= []
    result= [100, 100]

    for i in range(len(dartResult)):
       temp.append(dartResult[i])

    i= 0
    while(i< len(temp)):
        if(i<len(temp)-1 and temp[i]=="1" and temp[i+1]=="0"):
            lst.append("10")
            i+=2
        else:
            lst.append(temp[i])
            i+=1

    while(len(lst)>0):
        print("lst=", lst)
        if(lst[0]=="*"):
            result[-1]= result[-1]*2
            result[-2]= result[-2]*2
            lst.pop(0)
        elif(lst[0]=="#"):
            result[-1]= result[-1]*(-1)
            lst.pop(0)
        else:
            if(lst[1]=="S"):
                result.append(int(lst[0]))
                lst.pop(0)
                lst.pop(0)
            elif(lst[1]=="D"):
                result.append(int(lst[0])**2)
                lst.pop(0)
                lst.pop(0)
            elif(lst[1]=="T"):
                result.append(int(lst[0])**3)
                lst.pop(0)
                lst.pop(0)

    result= result[2:]
    return sum(result)

## main ##
dartResult= "1S*2T*3S"
print(solution(dartResult))
