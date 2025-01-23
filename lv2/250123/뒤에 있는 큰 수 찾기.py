## 설마 단순구현? - 4개 시간초과
## max를 계속 찾자! - 실패, 더 느려짐


def solution_my(numbers):
    result= []
    for i in range(len(numbers)-1):
        flag = 0
        for j in range(i, len(numbers)):
            if(numbers[i]<numbers[j]):
                result.append(numbers[j])
                flag= 1
                break
        if(flag==0):
            result.append(-1)
    result.append(-1)

    return result

def solution(numbers):
    n = len(numbers)
    result = [-1] * n  # 결과 배열 (-1로 초기화)
    stack = []  # 뒷 큰수를 찾기 위한 스택

    for i in range(n - 1, -1, -1):  # 오른쪽에서 왼쪽으로 탐색
        # 현재 원소보다 작거나 같은 수를 스택에서 제거
        while stack and stack[-1] <= numbers[i]:
            stack.pop()
        # 스택의 맨 위에 있는 수가 뒷 큰수
        if stack:
            result[i] = stack[-1]
        # 현재 원소를 스택에 추가
        stack.append(numbers[i])

    return result




## main ##
numbers= [2, 3, 3, 5]
print(solution(numbers))