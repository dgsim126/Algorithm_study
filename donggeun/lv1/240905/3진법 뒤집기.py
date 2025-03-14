def solution(n):
    three= toThree(n)
    ten= toTen(three)

    return ten

def toThree(n):
    result= ""
    i= 1
    while(n>=3):
        tmp= n%3
        n= n//3
        result+= str(tmp)
    result+=str(n)

    return result

def toTen(n):
    result= 0
    tmp= len(n)-1
    for i in range(len(n)):
        result+=(3**(tmp) * int(n[i]))
        tmp-=1

    return result

## main ##
n= 125
print(solution(n))