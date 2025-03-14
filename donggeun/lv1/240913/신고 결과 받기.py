def solution(id_list, report, k):
    report = list(set(report))  # 중복 신고 제거
    id_dic = {i: 0 for i in id_list}  # (신고 받은 사람 : 신고된 횟수)
    report_dic = {i: [] for i in id_list}  # (신고 받은 사람 : 신고한 사람[]) - 초기화 방법 수정
    result = {i: 0 for i in id_list}  # (신고한 사람 : 메일 수)

    for r in report:
        reporter, criminal = r.split()
        id_dic[criminal] += 1
        if criminal in report_dic:
            report_dic[criminal].append(reporter)

    # 신고 횟수 기반으로 결과 리스트 업데이트
    for criminal, reporters in report_dic.items():
        if id_dic[criminal] >= k:
            for reporter in reporters:
                result[reporter] += 1  # 신고받은 유저가 정지되었을 때 메일 수 업데이트

    # 결과를 id_list 순서대로 반환
    answer = [result[user] for user in id_list]  # id_list 순서에 맞게 결과를 반환

    return answer

# 테스트
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 2
print(solution(id_list, report, k))
