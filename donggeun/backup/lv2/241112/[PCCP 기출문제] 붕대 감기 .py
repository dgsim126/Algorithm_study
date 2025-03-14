from collections import deque

def solution(bandage, health, attacks):
    max_health= health
    attacks= deque(attacks)
    current_t= 0
    flag= 0

    for i in range(attacks[-1][0]+1): # 마지막 몬스터의 공격까지 초(i)를 증가시킴
        # 현재 몬스터의 공격이 진행되는지 확인
        if(i==attacks[0][0]):
            health-=attacks[0][1]
            current_t= 0

            attacks.popleft()
            flag= 1

        # 몬스터의 공격이 없다면 시간 증가
        else:
            if(flag!=0):
                health+=bandage[1]
                current_t+=1
                flag=1

            # 시전 시간을 만족했을 때
            if(current_t==bandage[0]):
                current_t= 0
                health+=(bandage[2])
        if(health>=max_health):
            health=max_health

        print(f"{i}, {health}, {current_t}")

        # 탈출조건
        if(health<=0):
            return -1

    return health

## main ##
bandage = [5, 1, 5] # [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
health = 30
attacks = [[2, 10], [9, 15], [10, 5], [11, 5]]
print(solution(bandage, health, attacks))