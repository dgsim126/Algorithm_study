# gpt's help
def solution(msg):
    dic = {chr(64 + i): i for i in range(1, 27)}  # 사전 초기화 {'A': 1, 'B': 2, ... 'Z': 26}
    current_index = 27  # 다음에 사전에 추가될 색인 번호
    result = []

    i = 0
    while i < len(msg):
        length = 1
        # 사전에서 현재 입력과 일치하는 가장 긴 문자열 찾기
        while i + length <= len(msg) and msg[i:i + length] in dic:
            length += 1

        # 사전에 없는 부분을 찾았으므로, 마지막으로 매칭된 부분의 색인 번호 추가
        result.append(dic[msg[i:i + length - 1]])

        # 사전에 새로운 단어 추가 (만약 msg의 끝을 넘어가지 않는다면)
        if i + length - 1 < len(msg):
            dic[msg[i:i + length]] = current_index
            current_index += 1

        # i를 매칭된 문자열의 길이만큼 이동
        i += length - 1

    return result


# 테스트 실행
msg = "KAKAO"
print(solution(msg))  # [11, 1, 27, 15]
