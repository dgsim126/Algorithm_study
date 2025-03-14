def solution(numbers, hand):
    answer = ''
    # 각 버튼별 위치
    button_position = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    # 왼손 초기 위치
    left = [3, 0]
    # 오른손 초기 위치
    right = [3, 2]

    def set_left(number):
        nonlocal answer, left
        left = button_position[number]
        answer = answer + 'L'

    def set_right(number):
        nonlocal answer, right
        right = button_position[number]
        answer = answer + 'R'

    for number in numbers:
        # 왼쪽버튼 처리
        if number in [1, 4, 7]:
            set_left(number)
        # 오른쪽 버튼 처리
        elif number in [3, 6, 9]:
            set_right(number)
        # 가운데 버튼이라면
        else:
            # 왼손과 오른손의 거리 계산하기
            left_distance = abs(left[0] - button_position[number][0]) + abs(left[1] - button_position[number][1])
            right_distance = abs(right[0] - button_position[number][0]) + abs(right[1] - button_position[number][1])
            # 거리가 같다면
            if left_distance == right_distance:
                # 오른손잡이 일때
                if hand == 'right':
                    set_right(number)
                # 왼손잡이 일때
                else:
                    set_left(number)
            # 왼쪽이 거리가 짧다면
            elif left_distance < right_distance:
                set_left(number)
            # 오른쪽 거리가 짧다면
            else:
                set_right(number)
    # 결과 반환
    return answer


if __name__ == "__main__":
    numbers_list = [
        [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],
        [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    ]

    hand_list = [
        "right",
        "left",
        "right"
    ]

    result_list = [
        "LRLLLRLLRRL",
        "LRLLRRLLLRR",
        "LLRLLRLLRL"
    ]

    length = len(result_list)
    for i in range(length):
        answer = solution(numbers_list[i], hand_list[i])
        if answer == result_list[i]:
            print('{}번 정답입니다.'.format(i + 1))
        else:
            print('{}번 실패입니다.'.format(i + 1))
            print('{} != {}'.format(answer, result_list[i]))