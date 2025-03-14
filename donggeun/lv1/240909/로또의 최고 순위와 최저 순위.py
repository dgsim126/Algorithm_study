def solution(lotto, win_num):
    check= [0]*46
    correct= 0
    possible= 0
    possible_row= 0

    for num in win_num:
        check[num]+=2

    for num in lotto:
        check[num]+=1

    for i in range(1, len(check)):
        if(check[i]==3):
            correct+=1
        elif(check[i]==2):
            possible+=1

    zero= check[0]
    first_correct= correct

    if(zero<=possible):
        correct+=zero
    else:
        correct+=possible

    rankList= [6,6,5,4,3,2,1]

    return [rankList[correct], rankList[first_correct]]

## main ##
lottos= [44, 1, 0, 0, 31, 25] # [44, 0, 0, 31]
win_nums= [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))