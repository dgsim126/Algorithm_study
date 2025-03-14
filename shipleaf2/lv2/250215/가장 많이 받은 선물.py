def solution(friends, gifts):
    answer = 0
    dic = {}    #
    arr = []    # friends 각 index 다음 달 선물 개수
    dic2 = {}   # 선물 지수 계산
    for i in range(len(friends)):
        arr.append(0)
        dic2[friends[i]] = 0
    for i in friends:
        for j in friends:
            if i  == j:
                continue
            else:
                dic[i + ' ' + j] = 0
    for i in gifts:
        dic[i] = dic[i] + 1
        dic2[i.split()[0]] = dic2[i.split()[0]] + 1
        dic2[i.split()[1]] = dic2[i.split()[1]] - 1
    count = 0
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            if dic[friends[i] + ' ' + friends[j]] < dic[friends[j] + ' ' + friends[i]]:
                arr[j] += 1
            elif dic[friends[i] + ' ' + friends[j]] > dic[friends[j] + ' ' + friends[i]]:
                arr[i] += 1
            else:
                if dic2[friends[i]] > dic2[friends[j]]:
                    arr[i] += 1
                elif dic2[friends[i]] < dic2[friends[j]]:
                    arr[j] += 1
    answer = max(arr)
    return answer