def recursive(x_first, x_end, y_first, y_end): # 0, 3, 0, 3
    global lst

    flag= lst[x_first][y_first]
    for i in range(x_first, x_end+1):
        for j in range(y_first, y_end+1):
            if(flag!=lst[i][j]): # 모두 동일하지 않다는게 밝혀지면
                recursive(x_first, (x_first+x_end)//2, y_first, (y_first+y_end)//2) # 0, 1, 0, 1
                recursive(x_first, (x_first+x_end)//2, ((y_first+y_end)//2)+1, y_end) # 0, 1, 2, 3
                recursive(((x_first+x_end)//2)+1, x_end, y_first, (y_first+y_end)//2)  # 2, 3, 0, 1
                recursive(((x_first+x_end)//2)+1, x_end, ((y_first+y_end)//2)+1, y_end) # 2, 3, 2, 3
                return

    # 모두 동일하다면
    for i in range(x_first, x_end+1):
        for j in range(y_first, y_end+1):
            lst[i][j]= -1

    lst[x_first][y_first]= flag

def solution(arr):
    global lst
    lst= arr
    x_first= 0
    y_first= 0
    x_end= len(arr)-1
    y_end= len(arr)-1

    recursive(x_first, x_end, y_first, y_end)

    # print(lst) # [[1, 1, 0, -1], [1, 0, -1, -1], [1, 0, 0, 1], [1, 1, 1, 1]]

    cnt_0= 0
    cnt_1= 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if(lst[i][j]==0):
                cnt_0+=1
            elif(lst[i][j]==1):
                cnt_1+=1

    return [cnt_0, cnt_1]

## main ##
# arr= [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr= [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))