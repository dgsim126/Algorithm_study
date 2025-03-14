from itertools import permutations

def solution(k, dungeons):
    max = 0
    for comb in permutations(dungeons, len(dungeons)):
        count = 0
        current_hp = k
        for dungeon in comb:
            if current_hp >= dungeon[0]:
                current_hp -= dungeon[1]
                count += 1
            else:
                continue
        if count > max:
            max = count

    return max

print(solution(80,[[80,20],[50,40],[30,10]]))

