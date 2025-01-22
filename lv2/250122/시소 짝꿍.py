def solution(weights):
    answer = 0
    dic = {}

    # 몸무게 빈도 계산
    for i in weights:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    # 비율에 맞는 짝꿍 계산
    for i in dic:
        if dic[i] > 1: # 1:1
            answer += (dic[i] * (dic[i] - 1)) / 2 # 같은 사람끼리 짝이므로 중복 방지
        if i * 2 in dic: # 1:2
            answer += dic[i] * dic[2 * i]
        if i * 2 / 3 in dic: # 2:3
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic: # 3:4
            answer += dic[i] * dic[i * 3 / 4]

    return answer