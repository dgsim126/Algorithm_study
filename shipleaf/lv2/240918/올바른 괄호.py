# 첫 풀이 후 효율성 테스트에서 시간 초과 remove 함수 pop 함수로 변경 => 통과

def solution(s):
    list = []
    if s[0] == ')':
        return False
    else:
        list.append(0)
    for i in range(1,len(s)):
        if s[i] == ')':
            if list != []:
                list.pop()  # remove => pop으로 변경
            else:
                return False
        else:
            list.append(0)
    if list == []:
        return True
    else:
        return False
    return True

# 테스트
print(solution("(())()"))