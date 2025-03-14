# 공약수 전체 구하기
def check(A):
    result= []
    min_A= min(A)

    for i in range(2, int(min_A**(1/2))+1, 1): # 나눌 수(공약수 확인 값= i)
        flag= True
        for j in range(len(A)):
            if(A[j]%i!=0):
                flag= False
                break
        if(flag==True):
            result.append(i)

    flag = True
    for i in range(len(A)):
        if(A[i]%min_A!=0):
            flag=False
            break

    if(flag==True):
        result.append(min_A)
    result.append(1)

    print(result)
    return result

def check2(A, val_A):
    result= []
    for i in range(len(val_A)):
        flag=True
        for j in range(len(A)):
            if(A[j]%val_A[i]==0):
                flag= False
                break
        if(flag==True):
            result.append(val_A[i])
    return result


def solution(arrayA, arrayB):
    val_A= check(arrayA)
    val_B= check(arrayB)

    temp1= check2(arrayA, val_A)
    temp2= check2(arrayB, val_B)
    temp1.append(0)
    temp2.append(0)

    return max(max(temp1), max(temp2))

## main ##
arrayA= [10, 20]
arrayB= [5, 17]
print(solution(arrayA, arrayB))