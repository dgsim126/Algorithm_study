# 성공률 76.9
def solution(storey):
    answer = 0
    while storey:
        rest = storey % 10

        if rest > 5:
            answer += (10 - rest)
            storey += 10

        elif rest <= 5:
            answer += rest

        storey //= 10

    return answer

# 성공
def solution(storey):
    answer = 0
    while storey:
        rest = storey % 10

        # 나머지가 6 ~ 9인 경우 올림
        if rest > 5:
            answer += (10 - rest)
            storey += 10

        # 나머지가 0 ~ 4인 경우 내림
        elif rest < 5:
            answer += rest

        # 나머지가 5인 경우
        else:
            if (storey // 10) % 10 > 4: # 다음 자릿수가 5 이상일 경우
                storey += 10 # 더하는게 유리
            answer += rest

        storey //= 10

    return answer