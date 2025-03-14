def solution(price, money, count):
    answer = 0

    for i in range(1, count+1):
        answer += (price * i)
    money-=answer

    if(money>=0):
        return 0
    return -money

## main ##
price= 3
money= 20
count= 4
print(solution(price, money, count))