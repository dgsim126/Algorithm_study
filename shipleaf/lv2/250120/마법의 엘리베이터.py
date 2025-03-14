def solution(storey):
    answer = 0
    str_storey = str(storey)
    num_list = []
    for i in range(len(str_storey)):
        num_list.append(int(str_storey[i]))
    print(num_list)
    num_list.reverse()
    num_list.append(0)
    print(num_list)
    for i in range(len(num_list)):
        if num_list[i] >= 6:
            answer += (10-num_list[i])
            num_list[i+1] += 1
        elif num_list[i] == 0:
            continue
        else:
            answer += num_list[i]
    return answer

print(solution(16))
print(solution(2554))