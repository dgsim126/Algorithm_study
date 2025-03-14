# def solution(name):
#     answer = 0
#     if "A" not in name:
#         for i in range(len(name)):
#             if ord(i) > 78:
#                 answer += abs(ord(i) - 91)
#             elif ord(i) <= 78:
#                 answer += ord(i) - 65
#             answer += 1
#     else:

#     return answer

# print(ord("N"))

def solution(name):
    # 상하 조작 횟수 계산
    def up_down_moves(char):
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    n = len(name)
    answer = 0
    move = n - 1

    for i in range(n):
        # 상하 조작 횟수 추가
        answer += up_down_moves(name[i])

        # 좌우 이동 최적화 계산
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1

        # 왼쪽으로 돌아가는 경우와 비교
        move = min(move, i + n - next_i + min(i, n - next_i))

    # 좌우 이동 횟수 추가
    answer += move

    return answer
