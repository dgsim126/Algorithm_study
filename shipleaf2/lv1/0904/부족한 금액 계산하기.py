def solution(price, money, count):
    answer = 0
    total = 0
    for i in range(count):
        total += (i+1)*price
    if total > money:
        answer = total - money
    return answer