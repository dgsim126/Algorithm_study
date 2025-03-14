# chatgpt - 여분의 체육복을 가져온 학생이 도난당한 경우
def solution(n, lost, reserve):
    num_list = [1]*n
    for i in range(n):
        if i+1 in lost:
            num_list[i] -= 1
        if i+1 in reserve:
            num_list[i] += 1

    for i in range(n):
        if num_list[i] == 0:
            if i > 0 and num_list[i-1] == 2:
                num_list[i] += 1
                num_list[i-1] -= 1
            elif i < n-1 and num_list[i+1] == 2:
                num_list[i] += 1
                num_list[i+1] -= 1

    return num_list.count(1) + num_list.count(2)