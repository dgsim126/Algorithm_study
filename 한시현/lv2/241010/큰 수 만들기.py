# gpt
def solution(number, k):
    stack = []
    for num in number:
        # 스택이 비어 있지 않고, 마지막 숫자가 현재 숫자보다 작고, 제거할 수 있는 기회가 남아 있는 경우
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 제거할 기회가 남아 있으면 뒤에서부터 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)