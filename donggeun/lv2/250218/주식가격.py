'''
당연히 for문으로 푸는 건 아닌 거 같은데... -> 이게 맞네?
'''
'''
def solution(prices):
    result= []
    for i in range(len(prices)-1):
        flag= 0
        for j in range(i, len(prices)):
            if(prices[i]>prices[j]):
                flag= 1
                result.append(j-i-0)
                break
        if(flag==0):
            result.append(len(prices)-i-1)
    result.append(0)

    return result
'''


# 이게 더 취지에 맞는 것 같아서 찾아봄
def solution(prices):
    answer = [0] * len(prices)  # 결과 배열 초기화
    stack = []  # (가격이 떨어지지 않은 시점의 인덱스)를 저장할 스택

    for i, price in enumerate(prices):
        # 현재 가격이 스택의 마지막 가격보다 낮으면, 스택에서 제거하며 지속 시간 계산
        while stack and prices[stack[-1]] > price:
            j = stack.pop()  # 떨어진 가격의 인덱스
            answer[j] = i - j  # 지속 시간 저장

        stack.append(i)  # 현재 인덱스를 스택에 추가

    # 스택에 남아 있는 인덱스들은 끝까지 유지된 값이므로 처리
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer