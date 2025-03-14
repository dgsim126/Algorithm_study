# 문제의 핵심은 중복된 이름인 경우
def solution(participant, completion):
    dic = {}

    for i in range(len(participant)):
        if participant[i] in dic:
            dic[participant[i]] += 1
        else:
            dic[participant[i]] = 1

    for i in range(len(completion)):
        if completion[i] in dic:
            dic[completion[i]] -= 1

    for key, value in dic.items():
        if (value == 1):
            return key


## main ##
participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))