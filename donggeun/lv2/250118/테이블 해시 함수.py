def solution(data, col, row_begin, row_end):
    # 1. 데이터를 알맞게 정렬하기
    data.sort(key=lambda x: (x[col-1], -x[0]))
    # print(data)
    result= 0

    for i in range(row_begin, row_end+1):
        temp= data[i-1]
        S_i= 0
        for j in range(len(temp)):
            S_i+=temp[j]%i
        result^=S_i

    return result

## main ##
data= [[2,2,6],
       [1,5,10],
       [4,2,9],
       [3,8,3]]
col= 2 # 해당 열(col-1)을 기준으로 오름차순 정렬, 같을 경우 0번째 열로 내림차순
row_begin= 2
row_end= 3
print(solution(data, col, row_begin, row_end))