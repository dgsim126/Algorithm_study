def solution(clothes):
    answer = 1
    closet = {}
    for clothe in clothes:
        if clothe[1] not in closet:
            closet[clothe[1]] = 1
        else:
            closet[clothe[1]] += 1

    for key in closet.keys():
        answer *= (closet[key] + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))