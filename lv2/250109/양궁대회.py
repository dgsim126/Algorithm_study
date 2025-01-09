from itertools import combinations

def solution(n, info):
    win = False
    answer = []
    target_list = [i for i in range(11)]
    for combs in combinations(target_list, n):
        list = [0 for i in range(11)]
        for i in combs:
            list[10-i] += 1
        apeach = 0
        ryan = 0
        for i in range(len(info)):
            if info[i] >= list[i] and info[i] != 0:
                apeach += 10 - i
            elif info[i] < list[i]:
                ryan += 10 - i
            else:
                continue
        if ryan > apeach:
            win = True
            if answer == []:
                answer.append(list)
            else:
                for i in range(-1,-(len(list)+1)):
                    if answer[0][i] != 0 and list[i] != 0:
                        if answer[0][i] > list[i]:
                            break
                        else:
                            answer.pop(0)
                            answer.append(list)
                    elif answer[0][i] > 0:
                        break
                    else:
                        answer.pop(0)
                        answer.append(list)
    if not win:
        answer.append(-1)
    return answer

print(solution(5,[2,1,1,1,0,0,0,0,0,0,0]))