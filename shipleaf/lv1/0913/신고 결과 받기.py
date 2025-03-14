def solution(id_list, report, k):
    answer = []
    dic1 = {}
    dic2 = {}
    dic3 = {}
    report = set(report)
    for i in id_list:
        dic1[i] = []
        dic2[i] = 0
        dic3[i] = 0
    for i in report:
        dic1[i.split()[0]].append(i.split()[1])
        dic2[i.split()[1]] += 1
    for i, j in dic2.items():
        if j >= k:
            for n, m in dic1.items():
                if i in m:
                    dic3[n] += 1
    for i in dic3.items():
        answer.append(i[1])
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
