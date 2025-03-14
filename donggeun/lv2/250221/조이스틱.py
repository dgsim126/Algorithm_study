'''
왼쪽부터 이동할지, 오른쪽부터 이동할지를 결정해야 함
- 현 위치에서 왼쪽, 오른쪽 방향으로 돌면서 먼저 a를 마주하는 방향을 찾는다.
- 먼저 a를 만나는 방향의 반대 방향으로 움직여야 최소로 움직임이 가능하다.
'''

'''
from collections import deque

def solution(name):
    move_right= name[1:]
    move_left= name[-1:0:-1]
    direct= "right"

    for i in range(len(move_right)):
        if(move_right[i]=="A"):
            direct= "left"
            break
        if(move_left[i]=="A"):
            direct= "right"
            break

    move= []
    if(direct=="left"):
        move.append(name[0])
        move.append(move_left)
        move= "".join(move)
    else:
        move= name

    move= list(move)
    print(move)

    while(True):
        if(move[-1]=="A"):
            move.pop()
        else:
            break
    print(move)

    alpha= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    alpha_reverse= ['A', 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 
                    'N', 
                    'M', 'L', 'K', 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B']

    move= deque(move)

    cnt= len(move)-1
    while(move):
        temp= move.popleft()
        min_= min(alpha.index(temp), alpha_reverse.index(temp))
        cnt+=min_


    return cnt
'''


def solution(name):
    # 조이스틱 조작 횟수
    answer = 0

    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer