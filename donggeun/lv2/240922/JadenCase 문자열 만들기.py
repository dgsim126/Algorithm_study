def solution(s):
    lst = list(map(str, s.split(" ")))
    result = ""

    for i in range(len(lst)):
        if lst[i]:  # 빈 문자열이 아닐 때만 처리
            if lst[i][0].isalpha():
                front = lst[i][0].upper()
                end = lst[i][1:].lower()
                lst[i] = front + end
            else:
                front = lst[i][0]
                end = lst[i][1:].lower()
                lst[i] = front + end

    for i in range(len(lst)):
        if (i == len(lst) - 1):
            result += lst[i]
        else:
            result += (lst[i] + " ")

    return result

## main ##
s = " m"
print(solution(s))