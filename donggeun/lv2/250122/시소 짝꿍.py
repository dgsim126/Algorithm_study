# gpt's help
def solution(weights):
    # 각 몸무게의 빈도수를 저장할 딕셔너리
    weight_count = {}

    # 몸무게 빈도수 계산
    for weight in weights:
        if weight in weight_count:
            weight_count[weight] += 1
        else:
            weight_count[weight] = 1

    print(weight_count)

    # 가능한 거리 비율
    ratios = [(1, 1), (2, 3), (2, 4), (3, 4)]

    # 결과 변수
    result = 0

    # 각 몸무게에 대해 가능한 짝꿍 계산
    for weight in weight_count:
        freq = weight_count[weight]

        # 동일한 몸무게인 경우 (1:1 비율)
        if freq > 1:
            result += freq * (freq - 1) // 2  # nC2 조합 계산

        # 다른 비율에 대해 계산
        for r1, r2 in ratios:
            partner_weight = weight * r1 / r2  # 짝꿍이 될 수 있는 몸무게
            if partner_weight != weight and partner_weight.is_integer():  # 짝꿍 조건 확인
                partner_weight = int(partner_weight)
                if partner_weight in weight_count:
                    result += freq * weight_count[partner_weight]

    # 비율 중복 계산을 방지하기 위해 절반으로 나누기
    return result // 2

## main ##
weights= [100,180,360,100,270]
print(solution(weights))