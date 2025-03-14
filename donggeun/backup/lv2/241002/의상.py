def solution(clothes):
    # 의상 종류가 명시되어 있지 않기에 의상 종류를 key, 의상 이름을 value
    dic= {}

    for i in range(len(clothes)):
        if(clothes[i][1] not in dic.keys()):
            dic[clothes[i][1]]= 1
        else:
            dic[clothes[i][1]]+=1

    # print(dic) # {'headgear': 2, 'eyewear': 1}

    answer= 1
    for count in dic.values():
        answer*=(count+1) # (의상을 입는 경우 + 안 입는 경우(1))

    return answer-1 # 아무것도 입지 않은 상태(-1)


## main ##
clothes= [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))