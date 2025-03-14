# 뒷자리부터 맞추면 될 듯

def solution_1(storey): # 정답률 38.5 - 자릿수가 변화할 경우(올림이 생겨 숫자 단위가 커질 경우)를 포함x
    result= 0

    for i in range(len(str(storey))):
        temp= storey%10
        storey= storey//10
        next_temp= storey%10
        if(temp>5 or (temp==5 and next_temp>=5)):
            result+= (10-temp)
            storey+=1
        else:
            result+= (temp)

    return result

def solution(storey): # 성공
    result= 0

    while(storey>0):
        temp= storey%10
        storey= storey//10
        next_temp= storey%10
        if(temp>5 or (temp==5 and next_temp>=5)):
            result+= (10-temp)
            storey+=1
        else:
            result+= (temp)

    return result

## main ##
storey= 2554
print(solution(storey))