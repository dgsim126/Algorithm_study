# gpt's help
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    # 지원자 정보를 저장할 딕셔너리
    data = {}

    # 1. 모든 경우의 조합 생성 및 저장
    for i in info:
        info_split = i.split()
        score = int(info_split[-1])
        conditions = info_split[:-1]

        for r in range(5):  # 4개 항목의 모든 조합 (0~4개 선택)
            for comb in combinations(range(4), r):
                temp = conditions[:]
                for idx in comb:
                    temp[idx] = "-"  # 조합에 해당하는 조건을 '-'로 변경
                key = ''.join(temp)
                if key not in data:
                    data[key] = []
                data[key].append(score)
    print(data) # {'javabackendjuniorpizza': [150], '-backendjuniorpizza': [150], 'java-juniorpizza': [150], 'javabackend-pizza': [150], 'javabackendjunior-': [150, 80], '--juniorpizza': [150], '-backend-pizza': [150, 260], '-backendjunior-': [150, 80], 'java--pizza': [150], 'java-junior-': [150, 80], 'javabackend--': [150, 80], '---pizza': [150, 260], '--junior-': [150, 80], '-backend--': [150, 260, 80, 50], 'java---': [150, 80], '----': [150, 210, 150, 260, 80, 50], 'pythonfrontendseniorchicken': [210, 150], '-frontendseniorchicken': [210, 150], 'python-seniorchicken': [210, 150, 50], 'pythonfrontend-chicken': [210, 150], 'pythonfrontendsenior-': [210, 150], '--seniorchicken': [210, 150, 50], '-frontend-chicken': [210, 150], '-frontendsenior-': [210, 150], 'python--chicken': [210, 150, 50], 'python-senior-': [210, 150, 50], 'pythonfrontend--': [210, 150], '---chicken': [210, 150, 80, 50], '--senior-': [210, 150, 260, 50], '-frontend--': [210, 150], 'python---': [210, 150, 50], 'cppbackendseniorpizza': [260], '-backendseniorpizza': [260], 'cpp-seniorpizza': [260], 'cppbackend-pizza': [260], 'cppbackendsenior-': [260], '--seniorpizza': [260], '-backendsenior-': [260, 50], 'cpp--pizza': [260], 'cpp-senior-': [260], 'cppbackend--': [260], 'cpp---': [260], 'javabackendjuniorchicken': [80], '-backendjuniorchicken': [80], 'java-juniorchicken': [80], 'javabackend-chicken': [80], '--juniorchicken': [80], '-backend-chicken': [80, 50], 'java--chicken': [80], 'pythonbackendseniorchicken': [50], '-backendseniorchicken': [50], 'pythonbackend-chicken': [50], 'pythonbackendsenior-': [50], 'pythonbackend--': [50]}

    # 점수를 정렬 (이진 탐색을 위해)
    for key in data:
        data[key].sort()

    # 2. 쿼리 처리
    answer = []
    for q in query:
        q_split = q.replace(" and ", " ").split()
        q_conditions = q_split[:-1]
        q_score = int(q_split[-1])
        key = ''.join(q_conditions)

        # 해당 조건의 점수 리스트 가져오기
        if key in data:
            scores = data[key]
            # 이진 탐색으로 조건을 만족하는 점수 개수 찾기
            index = bisect_left(scores, q_score)
            answer.append(len(scores) - index)
        else:
            answer.append(0)

    return answer


## main ##
info= ["java backend junior pizza 150",
       "python frontend senior chicken 210",
       "python frontend senior chicken 150",
       "cpp backend senior pizza 260",
       "java backend junior chicken 80",
       "python backend senior chicken 50"]

query= ["java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"]

print(solution(info, query))