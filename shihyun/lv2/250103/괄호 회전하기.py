def solution(s):
    s_list = list(s)
    len_s = len(s_list)
    count = 0

    for _ in range(len_s):
        check_list = []

        for s_char in s_list:
            if check_list:
                if check_list[-1] == '(' and s_char == ')':
                    check_list.pop()
                elif check_list[-1] == '{' and s_char == '}':
                    check_list.pop()
                elif check_list[-1] == '[' and s_char == ']':
                    check_list.pop()
                else:
                    check_list.append(s_char)
            else:
                check_list.append(s_char)

        if not check_list:
            count += 1

        s_list.append(s_list.pop(0))

    return count