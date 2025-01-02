def solution(s):
    trans = 0
    total_0 = 0

    while True:
        count_0 = s.count('0')
        total_0 += count_0
        s = s.replace('0', '') # replace를 통한 반환값 저장 필요

        s = bin(len(s))[2:]
        trans += 1

        if s == '1':
            break

    answer = [trans, total_0]

    return answer