# 내림차순 정렬 -> n번째 값이 최초로 n을 넘지 않을 때, n-1이 H-Index 값이다. (?)
def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)): # H_index가 존재하고 H_index를 넘는 논문이 몇 개인지 구할때
        if (citations[i] < i + 1):
            return i

    return len(citations) # 인용 횟수가 모두 같을때는 전체를 return