def solution(s):
    s = s[2:-2]
    s = s.split("},{") # gpt : 집합을 문자열로 분리해서 리스트 생성

    # 짧은 문자열부터 정렬
    for i in range(len(s)):
        for j in range(0, len(s) - i - 1):
            if len(s[j]) > len(s[j + 1]):
                s[j], s[j + 1] = s[j + 1], s[j]

    result = []
    for i in s:
        list = i.split(',') # 리스트의 문자열 split, 리스트로 만듦
        for j in list: # 리스트 1개 요소씩 검사
            if int(j) not in result:
                result.append(int(j))

    return result