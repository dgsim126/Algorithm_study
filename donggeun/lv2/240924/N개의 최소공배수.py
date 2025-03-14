def solution(arr):

    result= arr[0]
    for i in range(1, len(arr)):
        result= to_find(result, arr[i])

    return result

def to_find(n1, n2):
    first_n1= n1
    first_n2= n2
    while(True):
        if(n1==n2):
            return n1
        if(n1<n2):
            n1+= (first_n1)
        else:
            n2+= (first_n2)

## main ##
arr= [1,2,3]
print(solution(arr))