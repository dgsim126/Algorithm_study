from itertools import combinations

def solution(relation):
    num_rows = len(relation)  # 행의 개수 (튜플 개수)
    num_cols = len(relation[0])  # 열의 개수 (속성 개수)
    candidate_keys = []  # 후보키를 저장할 리스트

    # nCr
    for r in range(1, num_cols + 1):
        # 현재 선택된 r개의 열 조합을 생성
        for cols in combinations(range(num_cols), r): # r개로 이루어진 조합을 만든다는 의미
            # 유일성 검사
            # 각 튜플에서 선택된 열(cols)에 해당하는 값만 추출하여 새로운 튜플을 생성
            unique_tuples = {tuple(row[col] for col in cols) for row in relation}
            print(unique_tuples)

            # 유일성을 만족하는지 확인
            # 유일성을 만족하려면 unique_tuples의 크기가 전체 튜플 수와 같아야 함
            if len(unique_tuples) == num_rows:
                # 최소성 검사
                # 현재의 열 조합(cols)이 기존 후보키의 부분집합인 경우를 검사
                is_minimal = True
                for key in candidate_keys:
                    # 기존 후보키 중 하나가 현재 조합(cols)의 부분집합이면 최소성을 만족하지 않음
                    if set(key).issubset(cols):
                        is_minimal = False
                        break

                # 최소성을 만족할 경우, 후보키 리스트에 추가
                if is_minimal:
                    candidate_keys.append(cols)

    # 최종적으로 찾은 후보키의 개수를 반환
    return len(candidate_keys)
## main ##
relation= [["100","ryan","music","2"],
           ["200","apeach","math","2"],
           ["300","tube","computer","3"],
           ["400","con","computer","4"],
           ["500","muzi","music","3"],
           ["600","apeach","music","2"]]
print(solution(relation))