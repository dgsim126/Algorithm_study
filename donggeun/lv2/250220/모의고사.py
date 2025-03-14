def solution(answers):
    first = [1, 2, 3, 4, 5]  # 5
    second = [2, 1, 2, 3, 2, 4, 2, 5]  # 8
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10

    first_cnt = 0
    second_cnt = 0
    third_cnt = 0

    for i in range(len(answers)):
        first_val = first[i % 5]
        second_val = second[i % 8]
        third_val = third[i % 10]

        if (answers[i] == first_val):
            first_cnt += 1
        if (answers[i] == second_val):
            second_cnt += 1
        if (answers[i] == third_val):
            third_cnt += 1

    result = []
    max_ = max(first_cnt, second_cnt, third_cnt)

    if (first_cnt == max_):
        result.append(1)
    if (second_cnt == max_):
        result.append(2)
    if (third_cnt == max_):
        result.append(3)
    return result
