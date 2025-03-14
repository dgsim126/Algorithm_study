def solution(citations):
    dic = {}    # 각 인용횟수에 해당하는 논문이 몇 개인지 체크
    for i in citations:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    citations = list(set(citations))
    citations.sort()
    citations.reverse() # 논문 중복 제거 및 내림차순 정렬, 가장 높은 인용 수부터 계산

    print(dic)
    print(citations)

    if dic[citations[0]] >= citations[0]:   # 가장 많이 인용된 논문 수가 바로 h이상이라면 return
        return citations[0]
    
    for i in range(1, len(citations)):
        sum = dic[citations[i]]
        if sum >= citations[i]:
            return citations[i]
        for j in range(i-1,-1,-1):
            sum += dic[citations[j]]
        if sum >= citations[i]:
            return citations[i]
        
    return 0

print(solution([3, 0, 6, 1, 5]))
print(solution([6,6,3,1,2,5]))