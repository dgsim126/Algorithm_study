# gpt
def solution(id_list, report, k):
    # 각 사용자가 신고한 유저를 저장하는 딕셔너리 (중복 신고 방지를 위해 set이 더 효율적)
    user_reports = {user: [] for user in id_list}
    
    # 신고 횟수를 기록할 딕셔너리
    report_count = {user: 0 for user in id_list}

    for rep in report:
        reporter, target = rep.split(' ')
        
        # 중복 신고 방지 (이미 신고한 대상이 리스트에 있는지 확인 후 추가)
        if target not in user_reports[reporter]:
            user_reports[reporter].append(target)
            report_count[target] += 1

    # k번 이상 신고된 유저 목록 (정지 대상자 목록을 저장)
    banned_users = []
    for user, count in report_count.items():
        if count >= k:
            banned_users.append(user)

    # 각 사용자가 받은 메일 수 계산 (밴된 유저를 신고한 사용자에게 메일 전송)
    result = {user: 0 for user in id_list}
    for reporter in id_list: # 각 신고자를 순회하며 그들이 신고한 대상을 확인
        for target in user_reports[reporter]: # 신고자가 신고한 대상 찾음
            if target in banned_users: # 대상이 밴 당한 경우
                result[reporter] += 1 # 해당 신고자의 메일 수 1 증가
    
    return list(result.values())