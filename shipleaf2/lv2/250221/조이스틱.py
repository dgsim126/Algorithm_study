# print(solution("BBBBAAAABA"))   ### 반례
# 변경이 필요한 index를 미리 저장, 반복문에서 가까운 다음 index를 탐색 후 이동

from collections import deque

def solution(name):
    answer = 0
    w = len(name)
    change = deque([])
    name = list(name)
    current = ["A"] * w
    for i in range(1, w):
        if name[i] != "A":
            change.append(i)

    index = 0
    while change:
        if name[index] != current[index]:
            if ord(name[index]) <= 78:
                answer += ord(name[index]) - 65
                current[index] = name[index]
            else:
                answer += 91 - ord(name[index])
                current[index] = name[index]
    
        front = 0
        back = 0

        if index < change[0]:
            front = change[0] - index
        else:
            front = w - index + change[0]
        
        if index > change[-1]:
            back = index - change[-1]
        else:
            back = index + w - change[-1]

        if front <= back:
            index = change.popleft()
            answer += front
        else:
            index = change.pop()
            answer += back
        
        if ord(name[index]) <= 78:
            answer += ord(name[index]) - 65
            current[index] = name[index]
        else:
            answer += 91 - ord(name[index])
            current[index] = name[index]

    return answer

# GPT
def solution(name):
    n = len(name)
    answer = 0

    # 1. 알파벳 변경 최소화
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 2. 커서 이동 최소화
    min_move = n - 1  # 기본 이동 (오른쪽으로만 이동)
    
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':  # 연속된 A 찾기
            next_i += 1
        
        # 왼쪽으로 갔다가 돌아오는 경우
        move = i + n - next_i + min(i, n - next_i)
        min_move = min(min_move, move)

    answer += min_move
    return answer

print(solution("JEROEN"))
print(solution("JAN"))
