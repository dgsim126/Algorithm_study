# gpt
# 시간초과
def solution(numbers):
    numbers = list(map(str, numbers))
    
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
                # 두 문자열을 이어붙였을 때 비교하여 자리를 바꿈
                numbers[i], numbers[j] = numbers[j], numbers[i]
    
    largest_number = ''.join(numbers)
    
    # 모든 숫자가 0일 경우 0 반환
    if largest_number[0] == '0':
        return '0'
    
    return largest_number