def solution(orders, course):
    # 1. orders를 len 순서로 정렬
    orders= sorted(orders, key=len)
    print(orders) # ['AC', 'CDE', 'ACDE', 'BCFG', 'ABCFG', 'ACDEH']

    # 2. orders 리스트 안 문자열을 각기 또 다른 리스트로 변환
    lst= []
    for i in range(len(orders)):
        temp= list(orders[i])
        lst.append(temp)
    print(lst) # [['A', 'C'], ['C', 'D', 'E'], ['A', 'C', 'D', 'E'], ['B', 'C', 'F', 'G'], ['A', 'B', 'C', 'F', 'G'], ['A', 'C', 'D', 'E', 'H']]

    # 3. 내부 리스트를 순회하며 내 뒤에 나를 포함하는 리스트의 개수를 구한 후, 현 리스트 위치 끝에 cnt 추가
    for i in range(len(lst)-1):
        cnt= 0
        for j in range(i+1, len(lst)):
            flag= True
            point= lst[i]
            comparison= lst[j]

            for k in range(len(point)):
                if(point[k] not in comparison): # 들어있지 않다면
                    flag= False
                    break

            if(flag==True):
                cnt+=1
        if(cnt!=0):
            lst[i].append(cnt)

    print(lst) # [['A', 'C', 3], ['C', 'D', 'E', 2], ['A', 'C', 'D', 'E', 1], ['B', 'C', 'F', 'G', 1], ['A', 'B', 'C', 'F', 'G'], ['A', 'C', 'D', 'E', 'H']]

    # 4. 현재 리스트에서 맨 뒤 값이 문자열인 것은 제거
    result= []
    for i in range(len(lst)):
        if(isinstance(lst[i][-1], int)): # gpt's help
            result.append(lst[i][0:-1])

    print(result) # [['A', 'C'], ['C', 'D', 'E'], ['A', 'C', 'D', 'E'], ['B', 'C', 'F', 'G']]

    # 5. 각 리스트를 문자열로 병합
    for i in range(len(result)):
        result[i]= ''.join(result[i])

    print(result)

    # 6. course 배열에 없는 사이즈 제거
    result = [r for r in result if len(r) in course]

    # 7. 정렬
    return sorted(result)


## main ##
orders= ["XYZ", "XWY", "WXA"]
course= [2,3,4]
print(solution(orders, course))