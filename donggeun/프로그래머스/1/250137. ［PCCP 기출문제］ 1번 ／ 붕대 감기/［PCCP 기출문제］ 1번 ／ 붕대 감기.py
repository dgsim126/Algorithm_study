"""
- 모든 공격이 끝난 후 남은 체력을 return!

"""
from collections import deque

def solution(bandage, health, attacks):
    end_time = attacks[len(attacks) - 1][0]
    time= 0 # 현재 시간
    current_hp= health # 현재 피
    current_time= 0 # 기 모으기


    while(time<end_time):
        time+=1

        # 공격을 받게 될 경우
        if(attacks[0][0]==time):
            current_hp-=attacks[0][1]
            attacks.pop(0)
            current_time= 0
            print(f"time={time}, hp={current_hp}, 기모으기={current_time}, 공격받음!")


        # 공격을 받지 않을 경우
        else:
            flag= -1
            current_time+=1
            if(current_time==bandage[0]): # 스킬 발동
                print(current_time, bandage[0])
                current_hp+=(bandage[1]+bandage[2])
                current_time= 0
                flag= 1

            else:
                current_hp+=bandage[1]
                flag= 0

            if (flag == 1):
                print(f"time={time}, hp={current_hp}, 기모으기={current_time}, 스킬발동")
            else:
                print(f"time={time}, hp={current_hp}, 기모으기={current_time}, 무사")


            if(current_hp>health):
                current_hp= health

        if(current_hp<=0):
            return -1


    return current_hp


## main ##
bandage = [1, 1, 1] # [시전 시간(t), 초당 회복량(x), 추가 회복량(y)]
health = 	5
attacks = 	[[1, 2], [3, 2]]# [공격 시간, 피해량]
print(solution(bandage, health, attacks))
