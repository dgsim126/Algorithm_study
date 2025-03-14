def solution(sizes):
    small= []
    big= []

    for i in range(len(sizes)):
        if(sizes[i][0]<=sizes[i][1]):
            small.append(sizes[i][0])
            big.append(sizes[i][1])
        else:
            small.append(sizes[i][1])
            big.append(sizes[i][0])

    return max(small) * max(big)


## main ##
sizes= [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))