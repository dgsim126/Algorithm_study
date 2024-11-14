# gpt
from itertools import combinations

def solution(relation):
    # 열의 개수와 행의 개수
    n_columns = len(relation[0])
    n_rows = len(relation)
    
    # 모든 열 조합을 확인하기 위해 조합을 저장할 리스트
    candidate_keys = []
    
    # 1. 가능한 모든 열 조합을 크기별로 생성
    for r in range(1, n_columns + 1):
        for cols in combinations(range(n_columns), r):
            # 2. 유일성 검사
            # 각 행의 열 조합에 해당하는 값들을 추출해 set에 추가해 고유성을 판단
            unique_tuples = {tuple(row[col] for col in cols) for row in relation}
            if len(unique_tuples) == n_rows:  # 유일성을 만족
                # 3. 최소성 검사
                # candidate_keys에 최소성을 만족하지 않는 조합이 없는지 검사
                # A.issubset(B) : 집합 A가 집합 B의 부분 집합인지 검사
                if not any(set(key).issubset(cols) for key in candidate_keys):
                    candidate_keys.append(cols)
    
    # 4. 후보키 개수를 반환
    return len(candidate_keys)