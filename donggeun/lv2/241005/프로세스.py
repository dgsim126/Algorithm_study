def solution(priorities, location):
    # 현 리스트에서 max()를 이용해 가장 높은 값을 찾는다.
    # 현재위치(최초위치는 0)에서부터 해당 값과 같은 녀석을 찾는다.
    # 만약 없다면 0부터 현재위치까지 중 해당 값과 같은 녀석을 찾는다.
    # 찾은 후 해당 위치의 값은 0으로 변환한다.
    # 이때 만약 0으로 변환하는 index가 location과 같다면 결과를 반환한다.

    current_index= 0
    count= 0
    for _ in range(len(priorities)):
        current_max= max(priorities)
        if(current_max in priorities[current_index:len(priorities)]):
            temp= priorities[current_index:len(priorities)].index(current_max)
            current_index+=temp
            # print(f"count= {count+1}, max= {current_max}, index= {current_index}, in")
        else:
            current_index= priorities[0:current_index].index(current_max)
            # print(f"count= {count + 1}, max= {current_max}, index= {current_index}, out")
        priorities[current_index]= 0
        count+=1

        # 탈출조건
        if(current_index==location):
            return count


## main ##
priorities= [1, 1, 9, 1, 1, 1]
location= 0
print(solution(priorities, location))