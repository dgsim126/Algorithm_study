def solution(k, ranges):
    y_value= [k]
    lst= []

    while(k!=1):
        if(k%2==0):
            k= k//2
        else:
            k= k*3+1
        # print(k)
        y_value.append(k)

    # print(y_value) # [5, 16, 8, 4, 2, 1]

    for i in range(1, len(y_value)):
        lst.append((y_value[i-1]+y_value[i])/2)

    # print(lst) # [10.5, 12.0, 6.0, 3.0, 1.5]


    result= []
    for i in range(len(ranges)):
        flag= True
        can_pop= len(lst)
        temp= lst[:]

        pop_left= ranges[i][0]
        pop_right= abs(ranges[i][1])

        for _ in range(pop_left):
            if(can_pop==0):
                flag=False
                break
            else:
                temp.pop(0)
                can_pop-=1

        for _ in range(pop_right):
            if(can_pop==0):
                flag=False
                break
            else:
             temp.pop()
             can_pop-=1

        if(flag==False):
            result.append(-1.0)
        else:
            result.append(float(sum(temp)))

    # print(result)
    return result

## main ##
k= 5
ranges= [[0,0],[0,-1],[2,-3],[3,-3]] # [33.0, 31.5, 0.0, -1.0]
print(solution(k, ranges))