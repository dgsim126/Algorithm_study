"""
푸는데 50분! 개빡치네
- 선물을 가장 많이 받을 친구가 받게 될 선물의 수
1. 두 사람이 선물을 주고받았다면 더 많이 선물을 준 사람이 선물을 받음
2. 두 사람이 선물을 주고받지 않았다면, 선물지수가 더 큰 사람이 선물을 받음
3. 선물 지수가 같다면, 선물을 주고받지 않음
사람이 n명이라면 3번의 경우가 없을 경우 다음달 선물의 수는 (n-1)!

"""
def solution(friends, gifts):
    # 선물지수 딕셔너리
    gift= {}
    for i in range(len(friends)):
        gift[friends[i]]= 0

    for i in range(len(gifts)):
        sender, receiver = gifts[i].split(" ")
        gift[sender]+=1
        gift[receiver]-=1
    print(gift) # {'muzi': -3, 'ryan': 2, 'frodo': 0, 'neo': 1}


    dic= {}

    for i in range(len(gifts)):
        move= gifts[i]
        sender, receiver= gifts[i].split(" ")
        move_reverse= receiver+" "+sender

        if(move in dic):
            dic[move]+=1
        elif(move_reverse in dic):
            dic[move_reverse]-=1
        else:
            dic[move]= 1

    print(dic) # {'muzi frodo': 1, 'ryan muzi': 3, 'frodo ryan': 1, 'neo muzi': 1}

    for i in range(len(friends)-1):
        for j in range(i+1, len(friends)):
            move= friends[i]+" "+friends[j]
            move_reverse= friends[j]+" "+friends[i]
            if (move not in dic and move_reverse not in dic):
                dic[move] = 0

    print(dic) # {'muzi frodo': 1, 'ryan muzi': 3, 'frodo ryan': 1, 'neo muzi': 1, 'ryan neo': 0, 'frodo neo': 0}

    dic_2= {}
    for key, value in dic.items():
        sender, receiver= key.split(" ")
        if(value>0):
            if(sender in dic_2):
                dic_2[sender]+=1
            else:
                dic_2[sender]=1
        elif(value<0):
            if (receiver in dic_2):
                dic_2[receiver] += 1
            else:
                dic_2[receiver] = 1
        else: # 서로 주고받지 못한 경우 누구의 선물지수가 더 높은지 확인해야 함
            if(gift[sender]>gift[receiver]):
                if (sender in dic_2):
                    dic_2[sender] += 1
                else:
                    dic_2[sender] = 1
            elif(gift[sender]<gift[receiver]):
                if (receiver in dic_2):
                    dic_2[receiver] += 1
                else:
                    dic_2[receiver] = 1

    print(dic_2) # {'muzi': 1, 'ryan': 2, 'frodo': 1, 'neo': 2}

    result= 0
    for key, value in dic_2.items():
        if(value>result):
            result= value

    return result


## main ##
friends= ["muzi", "ryan", "frodo", "neo"]
gifts= ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
print(solution(friends, gifts))