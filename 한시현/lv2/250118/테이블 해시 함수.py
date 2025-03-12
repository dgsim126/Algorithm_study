def solution(data, col, row_begin, row_end):
    # 1. 데이터 정렬
    data.sort(key=lambda x: (x[col - 1], -x[0]))

    # 2. 해시 값 계산
    hash_value = 0
    for i in range(row_begin, row_end + 1):
        # i번째 행에서 S_i 계산
        row = data[i - 1]  # 행 번호는 1부터 시작, 인덱스는 0부터 시작

        S_i = sum(value % i for value in row)

        # XOR 연산 누적
        hash_value ^= S_i

    return hash_value