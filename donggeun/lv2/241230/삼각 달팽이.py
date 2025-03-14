def down(lst, x_min, x_max, y_min, y_max):
    global cnt, x, y
    for i in range(x_min, x_max+1):
        lst[i][y_min]= cnt
        cnt+=1

def right(lst, x_min, x_max, y_min, y_max):
    global cnt, x, y
    for i in range(y_min, y_max+1):
        lst[x_max][i]= cnt
        cnt+=1

def up(lst, x_min, x_max, y_min, y_max):
    global cnt, x, y
    temp= x_max-x_min
    temp_x= x_max
    temp_y= y_max
    for i in range(temp+1):
        lst[temp_x][temp_y]= cnt
        temp_x-=1
        temp_y-=1
        cnt+=1


def solution(n):
    # 배열 초기화
    lst= []
    for i in range(n):
        lst.append([0]*(i+1))

    # 전역 변수 설정
    global cnt, x, y
    cnt= 1
    x= 0
    y= 0

    # 지역 변수 설정
    x_min= 0
    x_max= n-1
    y_min= 0
    y_max= n-1

    for i in range(n):
        if(i%3==0):
            down(lst, x_min, x_max, y_min, y_max)
            x_min += 1
            y_min += 1
        elif(i%3==1):
            right(lst, x_min, x_max, y_min, y_max)
            x_max -= 1
            y_max -= 1
        else:
            up(lst, x_min, x_max, y_min, y_max)
            x_min += 1
            y_max -= 1


    # while(2):
    #     down(lst, x_min, x_max, y_min, y_max)
    #     x_min+=1
    #     y_min+=1
    #
    #     right(lst, x_min, x_max, y_min, y_max)
    #     x_max-=1
    #     y_max-=1
    #
    #     up(lst, x_min, x_max, y_min, y_max)
    #     x_min+=1
    #     y_max-=1
    #
    #     down(lst, x_min, x_max, y_min, y_max)
    #     x_min += 1
    #     y_min += 1
    #
    #     right(lst, x_min, x_max, y_min, y_max)
    #     x_max -= 1
    #     y_max -= 1
    #
    #     up(lst, x_min, x_max, y_min, y_max)
    #     x_min += 1
    #     y_max -= 1
    #
    #     print(x_min, x_max, y_min, y_max)
    #
    #     break

    result = []
    for inside in lst:
        for value in inside:
            result.append(value)
    return result



## main ##
n= 5
print(solution(n))