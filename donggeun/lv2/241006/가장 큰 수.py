# dfs로 모든 경우를 구하고, heapq 사용. (실패: heapq는 맨 앞의 값을 가장 작게 해줄 뿐 정렬 상태 X)
# gpt's help
# 3번 반복이 충분한 이유: 숫자의 길이가 1~4 자리일 때, 각 숫자를 3번 반복하면 어떤 조합이든 충분히 비교가 가능

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True) # sort 관련 암기할 것
    result = ''.join(numbers)
    return str(int(result))

## main ##
numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

## main ##
numbers= [3, 30, 34, 5, 9]
print(solution(numbers))