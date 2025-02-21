# gpt
def solution(name):
    move = 0  # 알파벳을 변경하는 조작 횟수
    length = len(name)

    # 1. 알파벳 변경 최소 횟수 계산
    for char in name:
        move += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 2. 커서 이동 최소 횟수 계산 (기본적으로 오른쪽으로만 가는 경우)
    min_move = length - 1

    # 3. 연속된 'A'가 나오는 지점 찾기 (변경하려면 이름에 A가 연속으로 들어간 경우)
    for i in range(length):
        next_index = i + 1
        while next_index < length and name[next_index] == 'A':
            next_index += 1

        # 왼쪽으로 갔다가 되돌아오는 경우 vs 오른쪽으로 가는 경우 비교
        min_move = min(min_move, 2 * i + (length - next_index), i + 2 * (length - next_index))

    return move + min_move