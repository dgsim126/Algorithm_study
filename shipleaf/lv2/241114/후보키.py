# def solution(relation):
#     answer = 0
#     dic = {}
#     for i in range(len(relation[0])):
#        dic[i] = []
#     for tuple in relation:
#         for i in range(len(tuple)):
#             dic[i].append(tuple[i])
#     for key, value in dic.items():
#         if len(value) > len(set(value)):
#             del dic[key]
#         else:
#             answer += 1
#     dic1 = dic
#     while True:
#         if len(dic) <= 1:
#             break
#         root = 0
#         next = 1
#         candidateKey = findCandidateKey(dic1[root], dic1[next])
#         if candidateKey == 0:
#             root += 1
#             next = root + 1
#         else:
#             next += 1
#     return answer
#
# def findCandidateKey(list1, list2):
#     candidateKey = []
#     for i in range(len(list1)):
#         candidateKey.append(list1[i]+list2[i])
#     if len(candidateKey) > set(len(candidateKey)):
#         return candidateKey
#     else:
#         return 0
#
# print(solution([["100","ryan","music","2"],
#                 ["200","apeach","math","2"],
#                 ["300","tube","computer","3"],
#                 ["400","con","computer","4"],
#                 ["500","muzi","music","3"],
#                 ["600","apeach","music","2"]]))

## GG

## GPT

from itertools import combinations

def solution(relation):
    n_rows = len(relation)  ## 행의 개수
    n_cols = len(relation[0])   ## 칼럼의 개수
    candidate_keys = []

    for i in range(1, n_cols + 1):
        for cols in combinations(range(n_cols), i):
            # 해당 컬럼 조합으로 각 튜플의 값 생성
            temp = [tuple(item[col] for col in cols) for item in relation]

            # 유일성 검사: 튜플의 조합 결과가 유일한지 확인
            if len(set(temp)) == n_rows:  # 모든 행이 고유하면 유일성 만족
                # 최소성 검사: 기존 후보키 중 하나가 이미 포함된 경우는 무시
                if not any(set(c).issubset(cols) for c in candidate_keys):
                    candidate_keys.append(cols)

    return len(candidate_keys)


# 예제 테스트
print(solution([["100", "ryan", "music", "2"],
                ["200", "apeach", "math", "2"],
                ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"],
                ["600", "apeach", "music", "2"]]))  # 결과: 2
