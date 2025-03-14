def solution(dirs):
    # 좌표평면에서 위치를 이동시키며 이동한 곳은 [[x,y],[x_2, y_2]] 이동 경로를 set에 넣기
    # set의 개수 구하기

    location= [0, 0]
    path= set()

    for i in range(len(dirs)):
        before = location[:]
        if(dirs[i]=="U"):
            location[1]+=1
        elif(dirs[i]=="R"):
            location[0]+=1
        elif(dirs[i]=="D"):
            location[1]-=1
        else:
            location[0]-=1

        # 범위 밖으로 나갈 경우 무효 처리
        if not (-5 <= location[0] <= 5 and -5 <= location[1] <= 5):
            location = before
            continue

        after = location
        path.add((before[0], before[1], after[0], after[1]))
        path.add((after[0], after[1], before[0], before[1]))
    return len(path)//2


## main ##
dirs= "ULURRDLLU"
print(solution(dirs))