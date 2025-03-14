def solution(number, k):
    stack = []
    for num in number:
        # 스택의 마지막 숫자가 현재 숫자보다 작고, 아직 제거할 숫자가 남아있다면 제거
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 만약 아직 제거하지 못한 숫자가 남아있다면 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]

    # 스택을 문자열로 변환하여 결과 반환
    return ''.join(stack)


# 테스트
number = "4177252841"
k = 4
print(solution(number, k))  # 예상 결과: "775841"
