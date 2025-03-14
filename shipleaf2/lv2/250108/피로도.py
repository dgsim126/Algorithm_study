from itertools import permutations

def solution(k, dungeons):
    answer = []
    list = [i for i in range(len(dungeons))]
    for combs in permutations(list, len(dungeons)):
        count = 0
        hp = k
        for i in combs:
            if hp >= dungeons[i][0]:
                count += 1
                hp -= dungeons[i][1]
            else:
                continue
        if count == len(dungeons):
            return count
        answer.append(count)
    return max(answer)
print(solution(80, [[80,20],[50,40],[30,10]]))
