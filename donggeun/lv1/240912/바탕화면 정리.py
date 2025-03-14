def solution(wallpaper):
    # 각 #의 좌표를 저장해야 함.
    lst_x= []
    lst_y= []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if(wallpaper[i][j]=="#"):
                lst_x.append(i)
                lst_y.append(j)

    # 드래그할 범위 구하는 법(lst에서 가장 큰, 가장 작은 x좌표, y좌표를 구한다)
    lst_x.sort()
    lst_y.sort()


    return [lst_x[0], lst_y[0], lst_x[-1]+1, lst_y[-1]+1]



## main ##
wallpaper= [".#...", "..#..", "...#."]
print(solution(wallpaper))