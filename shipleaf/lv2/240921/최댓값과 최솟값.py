def solution(s):
    answer = ''
    num_list = []
    for i in range (len(s.split())):
        num_list.append(int(s.split()[i]))
    answer = str(min(num_list)) + " " + str(max(num_list))
    return answer

# 테스트
print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))