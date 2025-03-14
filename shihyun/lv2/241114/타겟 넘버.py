def solution(numbers, target):
    list = [0]

    for num in numbers:
        temp = []
        for l in list:
            temp.append(l + num)
            temp.append(l - num)
        list = temp

    return list.count(target)

# 시간 초과
# def solution(numbers, target):
#     numlen = len(numbers)
#     list = [numbers[0], -numbers[0]]

#     for i in range(1, numlen):
#         for _ in range(len(list)):
#             current_num = list.pop(0)
#             list.append(current_num + numbers[i])
#             list.append(current_num - numbers[i])

#     return list.count(target)