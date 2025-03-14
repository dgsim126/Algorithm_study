def solution(n, lost, reserve):
    cnt= 0

    ## 초기화 작업
    student= [1]*n                  # 모든 학생들이 체육복 한 벌을 가진 것으로 초기화
    for i in range(len(lost)):      # 체육복이 없는 학생들을 0으로 초기화
        student[lost[i]-1]-=1
    for i in range(len(reserve)):   # 여벌 체육복이 있는 학생들 2로 초기화
        student[reserve[i]-1]+=1

    print(student)

    ## 그리디 수행
    for i in range(0, len(student)):
        if(i==0):
            if (student[i] == 2 and student[i + 1] == 0):
                student[i] = 1
                student[i + 1] = 1
            else:
                continue
        if (i == len(student)-1):
            if (student[i]==2 and student[i-1]==0):
                student[i] = 1
                student[i - 1] = 1
            else:
                continue

        if(student[i]==2 and student[i-1]==0):      # 현재 위치의 값이 2이고 앞이 0이면 가져옴
            student[i]= 1
            student[i-1]= 1
        elif(student[i]==2 and student[i+1]==0):    # 현재 위치의 값이 2이고 뒤가 0이면 가져옴
            student[i]= 1
            student[i+1]= 1
        else:
            continue

    print(student)

    ## 체육복이 있는 학생 수를 세는 과정
    for i in student:
        if(i>=1):
            cnt+=1
    return cnt


## main ##
n= 8
lost= [1,3,5,7]
reserve= [2,4,6,8]
print(solution(n, lost, reserve))