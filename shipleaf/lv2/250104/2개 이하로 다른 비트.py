from itertools import product

def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(functionX(number))
    return answer

def functionX(number):
    min = 10**15
    bin_len = len(bin(number)[2:])
    bin_num = bin(number)[2:]
    arr = "01"
    for combs in product(arr, repeat=bin_len+1):
        str_combs = ""
        for str in combs:
            str_combs += str
        if int(str_combs, 2) > number:
            if len(str_combs) != len(bin_num):
                bin_num = "0" + bin_num
        else:
            continue
        count = 0
        for i in range(len(str_combs)):
            count += abs(int(str_combs[i]) - int(bin_num[i]))
        if int(str_combs, 2) < min and count <= 2:
            min = int(str_combs, 2)
    return min

print(solution([7]))
