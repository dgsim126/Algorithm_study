def cal(diffs, times, limit, level):
    result = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            result += times[i]
        else:
            if i == 0:
                result += times[i] * (diffs[i] - level + 1)
            else:
                result += ((times[i] + times[i - 1]) * (diffs[i] - level)) + times[i]

        if result > limit:  # 제한 시간을 초과하면 0 반환
            return 0
    return 1  # 제한 시간 내에 해결 가능하면 1 반환



def solution(diffs, times, limit):
    level_front= 0
    level_last= max(diffs)

    while(True):
        current_level= (level_front+level_last)//2
        if(level_last - level_front < 5):
            for i in range(level_front, level_last+1):
                if(cal(diffs, times, limit, i)==1):
                    return i


        else:
            if(cal(diffs, times, limit, current_level)==0): # 정답이 더 큰 범위이다.
                level_front= current_level+1
            else: # 정답이 더 작은 범위이다.
                level_last= current_level







## main ##
diff= [1, 4, 4, 2]  # 퍼즐 난이도
times= 	[6, 3, 8, 2]  # 퍼즐의 소요 시간
limit= 	59        # 전체 제한 시간
print(solution(diff, times, limit))