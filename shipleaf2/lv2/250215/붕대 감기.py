def solution(bandage, health, attacks):
    curren_health = health
    curren_health -= attacks[0][1]
    if curren_health <= 0:
        return -1
    for i in range(len(attacks)-1):
        next_attack, next_dmg = attacks[i+1][0], attacks[i+1][1]
        heal = ((next_attack - attacks[i][0] -1) // bandage[0]) * bandage[2] + ((next_attack - attacks[i][0] -1) * bandage[1])
        curren_health += heal
        if curren_health > health:
            curren_health = health
        curren_health -= next_dmg
        if curren_health <= 0:
            return -1
        if i == len(attacks) - 2:
            return curren_health

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]])) ## 5
print(solution([3, 2, 7],20,[[1, 15], [5, 16], [8, 6]])) ## -1
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]])) ## -1
print(solution([1,1,1],5,[[1,2],[3,2]]))