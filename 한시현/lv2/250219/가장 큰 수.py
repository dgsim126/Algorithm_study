def solution(numbers):
    numbers = list(map(str, numbers))

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    largest_number = ''.join(numbers)

    # gpt : 모든 숫자가 0일 경우 0 반환
    if largest_number[0] == '0':
        return '0'

    return largest_number


from functools import cmp_to_key

def compare(a, b):
    if a + b > b + a:
        return -1  # a를 앞에 둠
    else:
        return 1  # b를 앞에 둠

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(compare))  # 커스텀 정렬 (sort(key=cmp_to_key(비교 함수)))

    largest_number = ''.join(numbers)  # 정렬된 숫자를 문자열로 합침

    return '0' if largest_number[0] == '0' else largest_number  # 0만 여러 개 있는 경우 "0" 반환