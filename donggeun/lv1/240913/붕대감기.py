# 최대 체력 초과 방지(gpt's help)

def solution(bandage, health, attacks):
    max_health = health
    current_time = 0
    stack = 0
    wave = 0

    while health > 0:
        # 탈출 조건
        if wave == len(attacks):
            return health

        # 공격을 받았을 때
        if attacks[wave][0] == current_time:
            print("attacked!")
            health -= attacks[wave][1]
            wave += 1
            stack = 0
            current_time += 1

            if health <= 0:
                return -1
        else:
            # 공격을 받지 않았을 때
            if stack == bandage[0] - 1:
                print("not attacked and stack complete!")
                health += bandage[1] + bandage[2]
                if health > max_health:  # 최대 체력 초과 방지
                    health = max_health
                current_time += 1
                stack = 0
            else:
                print("not attacked")
                if health < max_health:
                    health += bandage[1]
                    if health > max_health:  # 최대 체력 초과 방지
                        health = max_health
                current_time += 1
                stack += 1

        print(f"현재 시간: {current_time - 1}, 현재 체력: {health}")
        print()

    return -1


## main ##
bandage = [1, 1, 1]  # [시전 시간, 초당 회복량, 추가 회복량]
health = 5
attacks = [[1, 2], [3, 2]]
print(solution(bandage, health, attacks))
