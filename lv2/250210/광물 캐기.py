def solution(picks, minerals):
    ratio = []
    index = 0
    d, i, s = 0, 0, 0
    while index < len(minerals):
        if minerals[index] == "diamond":
            d += 1
        elif minerals[index] == "stone":
            s += 1
        else:
            i += 1
        if index % 5 == 4:
            ratio.append([d,i,s])
            d, i, s = 0, 0, 0
        index += 1

    ratio.append([d,i,s])

    sorted_ratio = sorted(ratio, key=lambda x: (-x[0], -x[1]))

    able_picks = picks
    
    health = 0
    for mineral in sorted_ratio:
        if able_picks[0] > 0:
            able_picks[0] -= 1
            health += mineral[0] + mineral[1] + mineral[2]
        elif able_picks[1] > 0:
            able_picks[1] -= 1
            health += 5 * mineral[0] + mineral[1] + mineral[2]
        elif able_picks[2] > 0:
            able_picks[2] -= 1
            health += 25 * mineral[0] + 5 * mineral[1] + mineral[2]
        else:
            break

    return health

# print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]))
print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]))
print(solution([1, 0, 1], ["diamond", "diamond", "diamond", "diamond", "diamond",
                           "stone", "stone", "stone", "stone", "stone",
                           "diamond", "diamond", "diamond", "diamond", "diamond"]))
