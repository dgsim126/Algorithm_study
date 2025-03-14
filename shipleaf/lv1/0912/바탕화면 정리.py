def solution(wallpaper):
    answer = []
    min_X = 100
    min_Y = 100
    max_X = -1
    max_Y = -1
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                if i < min_Y:
                    min_Y = i
                if i > max_Y:
                    max_Y = i
                    print(i)
                if j < min_X:
                    min_X = j
                if j > max_X:
                    max_X = j
            print(min_Y,min_X,max_Y,max_Y)
    answer.append(min_Y)
    answer.append(min_X)
    answer.append(max_Y+1)
    answer.append(max_X+1)
    return answer

# 테스트
# print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))