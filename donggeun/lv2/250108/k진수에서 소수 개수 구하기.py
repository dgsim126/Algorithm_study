

def convert(n, k):
    result= ""
    while(n>0):
        result= str(n%k)+result
        n= n//k
    return result

def findPrime(value):
    result= []

    for i in range(len(value)):
        if(value[i]==""):
            continue
        if(value[i]=="1"):
            continue
        num= int(value[i])
        if(num == 2):
            result.append(2)
            continue
        if(num%2==0):
            continue

        flag= 1
        for j in range(3, int(num**(1/2))+1, 2):
            if(num%j==0):
                flag= 0
                break
        if(flag==1):
            result.append(value[i])

    return result




def solution(n, k):
    value= convert(n, k)
    value= value.split("0")
    # print(value) # ['211', '2', '1', '1', '11']

    return len(findPrime(value))







## main ##
n= 437674
k= 3
print(solution(n, k))