def solution(record):
    result= []
    answer= []
    dic= {}

    for i in range(len(record)):
        dummy= record[i].split(" ")
        if(len(dummy)==3):
            if(dummy[0]=="Enter"): # Enter일 때
                dic[dummy[1]]= dummy[2]
                result.append([1, dummy[1]])
            else:  # Change일 때
                dic[dummy[1]]= dummy[2]
        else: # Leave일 때
            result.append([0, dummy[1]])

    # print(result) # [['Enter', 'uid1234'], ['Enter', 'uid4567'], ['Enter', 'uid1234'], ['Enter', 'uid1234']]

    for i in range(len(result)):
        if(result[i][0]==1):
            answer.append(f"{dic[result[i][1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{dic[result[i][1]]}님이 나갔습니다.")

    return answer




## main ##
record= ["Enter uid1234 Muzi",
         "Enter uid4567 Prodo",
         "Leave uid1234",
         "Enter uid1234 Prodo",
         "Change uid4567 Ryan"]
print(solution(record))
