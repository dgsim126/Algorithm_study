def solution(array, commands):
    answer = []
    for command in commands:
        array2 = array[command[0]-1:command[1]:]
        array2.sort()
        answer.append(array2[command[2]-1])
    return answer