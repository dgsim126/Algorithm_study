# google, gpt's solution

def solution(n):
    answer = ''  # 결과를 저장할 문자열
    while n > 0:
        remainder = n % 3  # 3으로 나눈 나머지
        if remainder == 0:  # 나머지가 0이면
            answer = '4' + answer  # 124 나라에서 0 대신 4를 사용
            n = n // 3 - 1  # 몫에서 1을 빼줌
        else:
            answer = str(remainder) + answer  # 나머지가 1 또는 2인 경우 그대로 사용
            n //= 3  # 몫을 구해 계속 진행
    return answer

## main ##
n= 12
print(solution(n))