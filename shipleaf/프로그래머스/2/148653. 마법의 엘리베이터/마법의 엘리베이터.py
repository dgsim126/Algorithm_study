def solution(storey):
    answer = 0
    while storey > 0:
        digit = storey % 10  # 현재 자릿수
        next_digit = (storey // 10) % 10  # 다음 자릿수
        
        # 현재 자릿수를 0으로 만드는 방법 선택
        if digit > 5 or (digit == 5 and next_digit >= 5):  # 올림 처리
            answer += (10 - digit)  # 필요한 마법의 돌 수
            storey += (10 - digit)  # 올림
        else:  # 내림 처리
            answer += digit
            storey -= digit
        
        # 다음 자릿수로 이동
        storey //= 10
    
    return answer
