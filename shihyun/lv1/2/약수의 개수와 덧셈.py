def solution(left, right):
    answer = 0
    check = 1
    odd = []

    while check*check <= 1000:
        odd.append(check*check)
        check += 1

    for i in range(left, right+1):
        if i in odd:
            answer -= i
        else:
            answer += i

    return answer