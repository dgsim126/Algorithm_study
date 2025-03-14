# GPT

def solution(N, stages):
    answer = []
    dic1 = {}
    dic2 = {}
    for i in range(1, N+2):
        dic1[i] = 0
    for i in range(1, N+2):
        dic2[i] = 0
    print(dic1)
    for i in stages:
        dic1[i] = dic1[i] + 1
    print(dic1)
    sum = 0
    for i in range(N+1, 0, -1):
        sum += dic1[i]
        dic2[i] = sum
    print(dic2)
    for i in range(1, N+1):
        if dic2[i] == 0:
            dic1[i] = 0
        else:
            dic1[i] = dic1[i]/dic2[i]

    del dic1[N+1]
    sorted_keys = [k for k, v in sorted(dic1.items(), key=lambda item: item[1], reverse=True)]  ###

    answer = sorted_keys

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5, [1, 1, 1, 1]))    ###
