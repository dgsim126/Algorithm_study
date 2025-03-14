# gpt's help
def solution(name):
    # 알파벳 변경 횟수를 계산하는 함수
    def change_cost(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 각 문자를 바꾸는 데 드는 최소 횟수 합산
    total_moves = sum(change_cost(char) for char in name)




    # 커서 이동 최적화
    min_move = len(name) - 1  # 일단 오른쪽으로 쭉 가는 경우를 기본값으로 설정

    for i in range(len(name)):
        next_index = i + 1
        # 'A'가 연속된 부분을 건너뛰기 위해 최적의 이동 방법 계산
        while next_index < len(name) and name[next_index] == 'A':
            next_index += 1

        # 현재 위치까지 오른쪽으로 갔다가, 'A'를 건너뛰고 돌아오는 경우
        # i+i: 갔다가 원상복구 하는 경우, len(name)-next_index: 원점에서 왼쪽으로 이동하는 횟수(a까지)
        min_move = min(min_move, i + i + len(name) - next_index)

    return total_moves + min_move


## main ##
name = "JEROEN"
print(solution(name))  # 56

name = "JAN"
print(solution(name))  # 23
