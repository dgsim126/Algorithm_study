def solution(bandage, health, attacks):
    healcont = 0
    turn = 1
    maxhp = health

    while turn <= attacks[-1][0]:
        attacked = False

        for attack in attacks:
            if attack[0] == turn:
                attacked = True
                healcont = 0
                health -= attack[1]

                if health <= 0:
                    return -1

        if not attacked:
            healcont += 1
            
            if healcont == bandage[0]:
                health += (bandage[1] + bandage[2])
                healcont = 0
            else:
                health += bandage[1]

            if health > maxhp:
                health = maxhp

        turn += 1

    return health