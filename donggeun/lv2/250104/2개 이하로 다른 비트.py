# gpt's help
def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            # 짝수: x + 1이 답
            answer.append(x + 1)
        else:
            # 홀수: 가장 오른쪽의 0을 찾아 비트를 조작
            rightmost_zero = ~x & (x + 1)  # 가장 오른쪽 0 위치
            result = x + rightmost_zero - (rightmost_zero // 2)
            answer.append(result)
    return answer

## main ##
numbers= [2,7]
print(solution(numbers))