# google
def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)): # H_index가 존재하고 H_index를 넘는 논문이 몇 개인지 구할때
        if citations[i] < i+1:
            return i

    return len(citations) # 인용 횟수가 모두 같을때는 전체를 return

# 실패
# def solution(citations):
#     sat = []
#     for ci in citations:
#         count = 0
#         for i in range(len(citations)):
#             if ci <= citations[i]:
#                 count += 1
#         if ci <= count:
#             sat.append(ci)

#     return max(sat)