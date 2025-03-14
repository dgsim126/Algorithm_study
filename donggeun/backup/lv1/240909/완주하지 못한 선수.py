def solution(participant, completion):
    dic= {}

    for i in range(len(participant)):
        dic[participant[i]]= 0

    for i in range(len(participant)):
        dic[participant[i]]+=1

    for i in range(len(completion)):
        dic[completion[i]]-=1

    for key, value in dic.items():
        if(value>0):
            return key

## main ##
participant= ["mislav", "stanko", "mislav", "ana"]
completion= ["stanko", "ana", "mislav"]
print(solution(participant, completion))