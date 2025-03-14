def solution(left, right):
    sum_= 0

    for i in range(left, right+1):
        if(oddOrEven(i)==0):
            sum_-=i
        else:
            sum_+=i
    return sum_


def oddOrEven(num):
    for i in range(1,33):
        if(i*i==num):
            return 0

        if(i*i>num):
            return 1


## main ##
left= 24
right= 82
print(solution(left, right))


