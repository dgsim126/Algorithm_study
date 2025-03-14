# 효율성 테스트 실패
def solution(info, query):
    info_list = []
    query_list = []
    answer = []

    for i in info:
        i = i.split()
        info_list.append(i)

    for q in query:
        q = q.replace(" and", "")
        q = q.split()
        query_list.append(q)

    for q in query_list:
        count = 0
        for i in info_list:
            satisfy = True

            if int(i[4]) < int(q[4]):
                satisfy = False
                continue

            for j in range(4):
                if q[j] == '-':
                    continue
                if q[j] != i[j]:
                    satisfy = False
                    break

            if satisfy:
                count +=1

        answer.append(count)

    return answer