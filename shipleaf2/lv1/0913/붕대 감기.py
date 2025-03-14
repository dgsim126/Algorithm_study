def solution(bandage, health, attacks):
    answer = 0
    dic2 = {}
    arr = []
    arr2 = []
    for i in attacks:
        dic2[i[0]] = i[1]
    for i in attacks:
        arr2.append(i[0])
    arr.append(health)
    t = 0
    if len(attacks) >= 1:
        for i in range(1, attacks[-1][0]):
            heart = 0
            if arr[i-1] == health and i not in arr2:
                t = 0
                arr.append(health)
            elif arr[i-1] == health and i in arr2:
                t = 0
                heart = health - dic2[i]
                arr.append(heart)
                if heart <= 0:
                    break
            elif arr[i-1] < health and i not in arr2:
                t += 1
                if t == bandage[0]:
                    t = 0
                    heart = arr[i-1] + bandage[1] + bandage[2]
                else:
                    heart = arr[i-1] + bandage[1]
                    if heart > 30:
                        heart = 30
                arr.append(heart)
            elif arr[i-1] < health and i in arr2:
                t = 0
                heart = arr[i-1] - dic2[i]
                arr.append(heart)
                if heart <= 0:
                    break
        arr.append(arr[-1]-attacks[-1][1])
    else:
        arr.append(health)
    if arr[-1] <= 0:
        answer = -1
    else:
        answer = arr[-1]
    return answer

# 테스트

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))
print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
print(solution([4, 2, 7],20,[[1, 15], [5, 16], [8, 6]]))
