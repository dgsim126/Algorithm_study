def solution(numbers):
    str_number = []
    answer = ""
    for number in numbers:
        str_number.append(str(number))

    str_number.sort(reverse=True)

    for i in range(len(str_number)):
        answer += str_number[i]

    return answer

print(solution([6,10,2]))
print(solution([3, 30, 34, 5, 9]))