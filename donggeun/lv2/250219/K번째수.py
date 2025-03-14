def solution(array, commands):
    result = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1]
        temp = array[start:end]
        temp = sorted(temp)
        result.append(temp[commands[i][2] - 1])

    return result