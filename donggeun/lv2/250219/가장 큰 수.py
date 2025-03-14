def solution(numbers):
    number = []
    for i in numbers:
        number.append(str(i))

    number = sorted(number, key=lambda x: x * 3, reverse=True)  # gpt

    result = ""

    for i in range(len(number)):
        result += number[i]

    # print(result)

    if (result[0] == "0"):
        return "0"
    return result