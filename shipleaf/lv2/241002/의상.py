def solution(clothes):
    answer = 1
    closet = {}
    for i in clothes:
        closet[i[1]] = []
    for item in clothes:
        closet[item[1]].append(item[0])
    print(closet)
    for key in closet.keys():
        answer *= (len(closet[key]) + 1)
    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
