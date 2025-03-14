from itertools import combinations # gpt's help(combinations를 호출하기 위한 import문 검색)

def solution(nums):
    lst= list(combinations(nums, 3)) # [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]
    result= adding(lst)

    return result

def adding(lst):
    result= 0

    for i in range(len(lst)):
        sum_= sum(lst[i])
        flag= checkPrime(sum_)
        # print(sum_, flag)
        if(flag==1): # 1일 경우 소수
            result+=1

    return result

def checkPrime(num):
    # print(num)
    if(num==0):
        return 0
    elif(num<3):
        return 1
    else:
        for i in range(2, (num//2)+1): # for i in range(1,int(x**0.5)+1): (다른 사람 풀이)
            if(num%i==0):
                return 0
    return 1

## main ##
nums= [1,2,3,4]
print(solution(nums))




