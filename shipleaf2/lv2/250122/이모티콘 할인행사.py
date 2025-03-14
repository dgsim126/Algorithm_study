from itertools import product

def solution(users, emoticons):
    # 가능한 할인율: 10%, 20%, 30%, 40%
    discount_rates = [10, 20, 30, 40]
    best_subscribers = 0
    best_sales = 0

    # 모든 할인율 조합 탐색
    for discounts in product(discount_rates, repeat=len(emoticons)):
        subscribers = 0
        sales = 0

        # 각 사용자에 대해 구매/가입 여부 결정
        for user in users:
            user_discount_threshold, user_budget = user
            total_spent = 0

            for i, emoticon in enumerate(emoticons):
                discounted_price = emoticon * (100 - discounts[i]) // 100
                if discounts[i] >= user_discount_threshold:
                    total_spent += discounted_price

            # 사용자가 이모티콘 플러스에 가입하는 경우
            if total_spent >= user_budget:
                subscribers += 1
            else:
                sales += total_spent

        # 최적의 결과 갱신
        if subscribers > best_subscribers or (subscribers == best_subscribers and sales > best_sales):
            best_subscribers = subscribers
            best_sales = sales

    return [best_subscribers, best_sales]

# 테스트 케이스
users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))  # 출력 예시: [1, 5400]

print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]d))
