def solution(info, query):
    # 지원자 정보를 저장할 데이터 구조
    info_dict = {}

    # 지원자 정보 처리
    for data in info:
        # 지원자 데이터를 분리
        split_data = data.split()
        key_data = split_data[:-1]
        score = int(split_data[-1])

        # 키의 모든 조합을 생성
        for i in range(16):  # 2^4 = 16가지 조합
            temp_key = key_data[:]
            for j in range(4):
                if i & (1 << j):  # j번째 비트가 켜져 있으면 '-'
                    temp_key[j] = '-'
            key = ' '.join(temp_key)
            if key not in info_dict:
                info_dict[key] = []
            info_dict[key].append(score)

    # 점수를 오름차순으로 정렬
    for key in info_dict:
        info_dict[key].sort()

    # 결과 저장 리스트
    answer = []

    # 문의 조건 처리
    for q in query:
        # 조건에서 'and' 제거 및 공백 기준 분리
        q = q.replace(' and ', ' ').split()
        key = ' '.join(q[:-1])
        score = int(q[-1])

        # 점수 조건을 만족하는 지원자 수 계산
        if key in info_dict:
            scores = info_dict[key]
            # 이분 탐색 구현
            low, high = 0, len(scores)
            while low < high:
                mid = (low + high) // 2
                if scores[mid] >= score:
                    high = mid
                else:
                    low = mid + 1
            answer.append(len(scores) - low)
        else:
            answer.append(0)

    return answer
        

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info, query))