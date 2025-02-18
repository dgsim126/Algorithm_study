def solution(prices):
    answer = []
    pl = len(prices)

    for i in range(pl):
        if i == pl-1:
            answer.append(0)
            break

        count = 0
        for j in range(i + 1, pl):
            count += 1
            if prices[i] > prices[j]:
                break
        answer.append(count)

    return answer