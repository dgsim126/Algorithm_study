def solution(wallpaper):
    leny = len(wallpaper)
    lenx = len(wallpaper[0])
    filey = []
    filex = []
    for i in range(leny):
        for j in range(lenx):
            if wallpaper[i][j] == '#':
                filex.append(j)
                filey.append(i)

    return [min(filey), min(filex), max(filey)+1, max(filex)+1]