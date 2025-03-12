def solution(lottos, win_nums):
    count = 0
    for win_num in win_nums:
        if win_num in lottos:
            count += 1
    
    zeros = lottos.count(0)
    correctNum = [count+zeros, count]
    answer = []

    for case in correctNum:
        if case == 6:
            answer.append(1)
        elif case == 5:
            answer.append(2)
        elif case == 4:
            answer.append(3)
        elif case == 3:
            answer.append(4)
        elif case == 2:
            answer.append(5)
        else:
            answer.append(6)
            
    return answer