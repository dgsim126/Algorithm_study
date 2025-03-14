# 실패율 = (스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수) / (스테이지에 도달한 플레이어 수)

def solution(n, stages): # 5, [2, 1, 2, 6, 2, 4, 3, 3]
    arrived= [0]*n
    cleared= [0]*n

    for i in range(n):
        for j in range(len(stages)):
            if(i+1 <= stages[j]): # 실패율의 분모, arrived 구하기
                arrived[i]+=1
            if (i+1 == stages[j]): # 실패율의 분자, cleared 구하기
                cleared[i] += 1
        if(arrived[i]==0): # 0으로 나누는 부분을 고려를 안해서 런타임에러(63%). 고쳤으나 테스트 3개에서 타임 에러(88.9%)
            arrived[i]= 0
        else:
            arrived[i]= cleared[i]/arrived[i]

    return mySort(arrived)

def mySort(arr):
    dic= {}
    lst= []

    for i in range(len(arr)):
        dic[i+1]= arr[i]

    dic= sorted(dic.items(), key=lambda x: x[1], reverse=True) # google's help

    for i in range(len(arr)):
        lst.append(dic[i][0])

    return lst

## main ##
n= 5 # (1/8), (3/7), (2/4), (1/2), (0/1) 각 스테이지 별 실패율
stages= [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(n, stages))