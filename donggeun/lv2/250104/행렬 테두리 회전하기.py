def solution(rows, columns, queries):
    lst= []
    num= 1
    result = []
    for i in range(rows): # 2차원 리스트 생성
        temp= []
        for j in range(columns):
            temp.append(num)
            num+=1
        lst.append(temp)
    # print(lst)

    for i in range(len(queries)):
        # [2,2,5,4]의 경우 (x=2-1, y=2-1) -> (x=4-1 y=5-1)
        x_first= queries[i][1]-1 # 1
        y_first= queries[i][0]-1 # 1
        x_last= queries[i][3]-1 # 3
        y_last= queries[i][2]-1 # 4

        temp= []

        # 위
        for j in range(x_first, x_last+1):
            temp.append(lst[y_first][j])
            # print(lst[y_first][j])

        # 오른쪽
        for j in range(y_first+1, y_last+1):
            temp.append(lst[j][x_last])
            # print(lst[j][x_last])

        # 밑(역방향)
        for j in range(x_last-1, x_first-1, -1):
            temp.append(lst[y_last][j])
            # print(lst[y_last][j])

        # 왼쪽(역방향)
        for j in range(y_last-1, y_first, -1):
            temp.append(lst[j][x_first])
            # print(lst[j][x_first])

        # print(temp)
        last_ele= temp.pop()
        temp.insert(0, last_ele)
        result.append(min(temp))
        # print(temp)


        # 위
        for j in range(x_first, x_last + 1):
            lst[y_first][j]= temp.pop(0)
            # print(lst[y_first][j])


        # 오른쪽
        for j in range(y_first + 1, y_last + 1):
            lst[j][x_last]= temp.pop(0)
            # print(lst[j][x_last])

        # 밑(역방향)
        for j in range(x_last - 1, x_first - 1, -1):
            lst[y_last][j]= temp.pop(0)
            # print(lst[y_last][j])

        # 왼쪽(역방향)
        for j in range(y_last - 1, y_first, -1):
            lst[j][x_first]= temp.pop(0)
            # print(lst[j][x_first])

        # print(lst)
    return result

## main ##
rows= 6
columns= 6
queries= [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))