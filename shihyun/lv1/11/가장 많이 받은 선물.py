# gpt
# 로직 이해 미완
from itertools import combinations

def solution(friends, gifts):
    give = []
    get = []

    for gift in gifts:
        a, b = gift.split(' ')
        give.append(a)
        get.append(b)
    
    gift_score = {}
    for friend in friends:
        gift_score[friend] = give.count(friend) - get.count(friend)

    next_gift = {friend: 0 for friend in friends}

    # 친구 사이에 주고받은 선물 횟수를 기록 (미완)
    gift_history = {friend: {other_friend: 0 for other_friend in friends} for friend in friends}

    for gift in gifts:
        a, b = gift.split(' ')
        gift_history[a][b] += 1

    for comb in combinations(gift_score, 2): # dictionary의 키 값만 반환
        a, b = comb

        # a와 b가 서로에게 준 선물 횟수 비교 (미완)
        gifts_a_to_b = gift_history[a][b]
        gifts_b_to_a = gift_history[b][a]

        if gifts_a_to_b > gifts_b_to_a:
            next_gift[a] += 1
        elif gifts_b_to_a > gifts_a_to_b:
            next_gift[b] += 1
        else:
            score1 = gift_score[comb[0]]
            score2 = gift_score[comb[1]]
            if score1 != score2:
                if score1 > score2:
                    next_gift[comb[0]] += 1
                else:
                    next_gift[comb[1]] += 1

    return max(next_gift.values())