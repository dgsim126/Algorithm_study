def solution(queue1, queue2):
    max_trial = len(queue1)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)

    trial_1 = 0
    trial_2 = 0

    while queue1_sum != queue2_sum:
        if trial_1 == max_trial and trial_2 == max_trial:
            return -1
        if queue1_sum > queue2_sum:
            x = queue1.pop(0)
            queue2.append(x)
            queue1_sum -= x
            queue2_sum += x
            trial_1 += 1
        else:
            x = queue2.pop(0)
            queue1.append(x)
            queue2_sum -= x
            queue1_sum += x
            trial_2 += 1
    
    return trial_1 + trial_2

# print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
# print(solution([1, 1], [1, 5]))
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))