# 풀다가 꼬여서 날라감. 안타깝게도 아래 내용은 gpt가 작성해준 내용

def solution(friends, gifts):
    gifted = {}  # gifted = {"friend 이름": {"선물 준 친구 이름": 이 친구에게 준 선물 개수}}
    gift_idx = {}  # 선물 지수
    # 딕셔너리 초기화
    for friend in friends:
        gifted[friend] = {}
        gift_idx[friend] = 0

    for gift in gifts:
        t, f = gift.split(' ')  # t: 선물을 준 사람, f: 받은 사람
        if f in gifted[t]:
            gifted[t][f] += 1
        else:
            gifted[t][f] = 1
        # 선물 지수 반영
        gift_idx[t] += 1
        gift_idx[f] -= 1

    # 각자 받게 될 선물 개수
    will_get = [0 for _ in friends]  # friends 리스트 순서대로 저장
    for i in range(len(friends)):
        curr = friends[i]  # 인덱스 i에 해당하는 친구
        for j in range(i + 1, len(friends)):
            another = friends[j]  # 인덱스 j에 해당하는 친구
            # curr가 another에게 준 선물 개수
            a = gifted[curr][another] if another in gifted[curr] else 0
            # another가 curr에게 준 선물 개수
            b = gifted[another][curr] if curr in gifted[another] else 0

            if a > b:  # curr가 선물을 더 많이 줬다면
                will_get[i] += 1
            elif a < b:  # another가 선물을 더 많이 줬다면
                will_get[j] += 1
            elif a == b:  # 둘이 선물을 주고 받은 개수가 같다면 선물 지수 확인
                ai, bi = gift_idx[curr], gift_idx[another]
                if ai > bi:
                    will_get[i] += 1
                elif ai < bi:
                    will_get[j] += 1

    answer = max(will_get)
    return answer