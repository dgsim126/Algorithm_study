def convert(time):
    list(time)
    time = int(str(time[0:2])) * 60 + int(str(time[3:5]))
    return time

def convertReverse(time):
    minute= time/60
    second= time%60

    if(second<10 and minute<10):
        return "0" + str(int(minute)) + ":0" + str(second)
    elif(second<10):
        return str(int(minute)) + ":0" + str(second)
    elif(minute<10):
        return "0" + str(int(minute)) + ":" + str(second)
    else:
        return str(int(minute))+":"+str(second)


def solution(video_len, pos, op_start, op_end, commands):
    video_len= convert(video_len)
    pos= convert(pos)
    op_start= convert(op_start)
    op_end= convert(op_end)

    for i in range(len(commands)):
        # 처음 시작 지점이 오프닝 구간인 경우
        if (op_start <= pos and pos <= op_end):
            pos = op_end


        # 뒤로 10초 이동
        if(commands[i]=="prev"):
            pos-=10
            if(pos<10):
                pos= 0

            if(op_start <= pos and pos <= op_end):
                pos= op_end

        # 앞으로 10초 이동
        else:
            pos+=10
            if(pos>video_len-10):
                pos=video_len

            if(op_start <= pos and pos <= op_end):
                pos= op_end

    # if (op_start <= pos and pos <= op_end):
    #     pos = op_end
    return convertReverse(pos)


## main ##
video_len= "05:00"
pos= "01:30"
op_start= "01:00"
op_end= "02:00"
commands= ["next"]
# 동영상 길이, 기능 수행 전 위치, 오프닝 시작 시간, 오프닝 종료 시간, 사용자 입력 배열
print(solution(video_len, pos, op_start, op_end, commands))