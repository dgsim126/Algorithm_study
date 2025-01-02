def solution(s):
    if len(s) == 1:
        return 1
    answer = 1000
    rangeNum = len(s) // 2
    for i in range(1, rangeNum + 1):
        word = ""
        index = 0
        while len(s) > index:
            if index + i > len(s): # 남은 문자열이 부족할 때
                word += s[index:]
                break
            else:
                num = 1
                term = s[index:index+i]
                index += i
                while index + i <= len(s) and term == s[index:index+i]:
                    num += 1
                    index += i
                if num > 1:
                    word += str(num) + term
                else:
                    word += term
        if len(word) < answer:
            answer = len(word)
    return answer


print(solution("aabbaccc"))