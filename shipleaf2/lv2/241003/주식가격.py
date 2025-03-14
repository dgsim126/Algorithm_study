def solution(prices):
    answer = []
    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                t += 1
                break
            else:
                t += 1
        answer.append(t)
    return answer

print(solution([1, 2, 3, 2, 3]))