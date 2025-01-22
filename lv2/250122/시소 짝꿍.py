# from itertools import combinations

# def solution(weights):
#     answer = 0
#     ratio = [1.0, 4/3, 1.5, 2.0]

#     weights = sorted(weights)
    
#     for comb in combinations(weights, 2):
#         if (comb[1]/comb[0]) in ratio:
#             answer += 1

#     return answer

# print(solution([100,180,360,100,270]))

## GPT's

# from collections import Counter

# def solution(weights):
#     distance_ratios = [(1, 1), (2, 3), (2, 4), (3, 4)]
    
#     weight_count = Counter(weights)
#     result = 0

#     print(weight_count)

#     for weight in weight_count:
#         for num, den in distance_ratios:
#             target_weight = weight * num / den
#             if target_weight in weight_count:
#                 if weight == target_weight:
#                     result += weight_count[weight] * (weight_count[weight] - 1) // 2
#                 else:
#                     result += weight_count[weight] * weight_count[target_weight]

#     return result

# print(solution([100,180,360,100,270]))

def solution(weights):
    distance_ratios = [(1, 1), (2, 3), (2, 4), (3, 4)]
    
    weight_count = {}
    for i in weights:
        if i not in weight_count:
            weight_count[i] = 1
        else:
            weight_count[i] += 1

    result = 0

    for weight in weight_count:
        for num, den in distance_ratios:
            target_weight = weight * num / den
            if target_weight in weight_count:
                if weight == target_weight:
                    result += weight_count[weight] * (weight_count[weight] - 1) // 2
                else:
                    result += weight_count[weight] * weight_count[target_weight]

    return result

print(solution([100,180,360,100,270]))