# def solution(citations):
#     citations.sort(reverse=True)
#
#     for i in range(len(citations)):
#         if(i+1>=citations[i]):
#             return citations[i]


def solution(citations):
    citations.sort(reverse=True)

    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i

    return len(citations)


## main ##
# citations = [3, 0, 6, 1, 5]
# citations = [9,7,6,5,4,1,0]
citations = [8,8,7,6,1,1,1]
print(solution(citations))