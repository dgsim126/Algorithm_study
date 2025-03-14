# def solution(dartResult):
#     answer = 0
#     arr = ["D", "S", "T"]
#     num_dic = {"0" : 1, "1" : 1, "2" : 1, "3" : 1, "4" : 1, "5" : 1, "6" : 1, "7" : 1, "8" : 1, "9" : 1, "D" : 0, "S": 0, "T": 0, "#" : 0, "*" : 0, ".": 0}
#     arr2 = []   # dartResult의 값들을 배열에 정리
#     for i in range(len(dartResult)):
#         arr2.append(dartResult[i])
#     for i in range(0, len(arr2)-1):
#         if arr2[i] == "1":
#             if num_dic[arr2[i+1]] == 0:
#                 arr2.insert(i, "0")
#                 i += 1
#                 print(1)
#         elif num_dic[arr2[i]] == 1:
#             arr2.insert(i, "0")
#             i += 1
#             print(1)
#     print(arr2)
#     return answer

# solution("1S2D*3T")

# 위 코드에서 insert를 했을 때 index가 밀려 0이 반복적으로 더하지는 현상 발생 => GPT 도움

def solution(dartResult):
    answer = 0
    scores = []
    i = 0
    
    while i < len(dartResult):
        if dartResult[i] == '1' and i + 1 < len(dartResult) and dartResult[i + 1] == '0':
            score = 10
            i += 1
        else:
            score = int(dartResult[i])
        
        i += 1

        if dartResult[i] == 'S':
            score = score ** 1
        elif dartResult[i] == 'D':
            score = score ** 2
        elif dartResult[i] == 'T':
            score = score ** 3
        
        i += 1

        if i < len(dartResult) and (dartResult[i] == '*' or dartResult[i] == '#'):
            if dartResult[i] == '*':
                score *= 2
                if len(scores) > 0:
                    scores[-1] *= 2
            elif dartResult[i] == '#':
                score *= -1
            i += 1
        
        scores.append(score)
    
    answer = sum(scores)
    return answer

print(solution("1S2D*3T"))
