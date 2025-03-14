# gpt's help
from copy import deepcopy

def solution(expression):
    lst= [] # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
    current_num= ""
    operation= [["+", "*", "-"],["+", "-", "*"],
                ["-", "*", "+"],["-", "+", "*"],
                ["*", "-", "+"],["*", "+", "-"]] # 경우의 수는 최대 6개
    result= []

    # 1. 숫자, 연산자 각각 순서대로 리스트에 넣기
    for i in expression:
        if(i.isdigit()): # 현위치가 숫자인 경우
            current_num+=i
        else: # 현 위치가 연산자인 경우
            lst.append(current_num)
            lst.append(i)
            current_num= ""
    lst.append(current_num)

    # print(lst) # ['100', '-', '200', '*', '300', '-', '500', '+', '20']

    # 2. 연산 순서별로 계산
    for i in range(len(operation)):  # 6가지 경우
        temp= deepcopy(lst)
        for oper in operation[i]:
            j= 0
            while(j < len(temp)):
                if(temp[j]==oper):  # 연산자 발견
                    if oper == "-":
                        temp[j-1]= int(temp[j-1])-int(temp[j+1])
                    elif oper == "+":
                        temp[j-1]= int(temp[j-1])+int(temp[j+1])
                    else:
                        temp[j-1] = int(temp[j-1]) * int(temp[j+1])
                    temp.pop(j)
                    temp.pop(j)
                    j-=1  # 연산 후 인덱스를 조정
                else:
                    j+=1
        result.append(abs(temp[0]))
    return max(result)

## main ##
expression= "100-200*300-500+20"
print(solution(expression))