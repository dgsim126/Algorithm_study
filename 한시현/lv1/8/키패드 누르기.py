def solution(numbers, hand):
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    answer = ''
    leftx = 0
    lefty = 3
    rightx = 2
    righty = 3

    for number in numbers:
        lefthand = phone[lefty][leftx]
        righthand = phone[righty][rightx]
        leftdis = 0
        rightdis = 0
        numx = -1
        numy = -1

        for i in range(len(phone)):
            for j in range(len(phone[0])):
                if number == phone[i][j]:
                    numx = j
                    numy = i
                    break
            if numx != -1:
                break

        if number in [1,4,7]:
            leftx = numx
            lefty = numy
            answer += 'L'
            continue
        elif number in [3,6,9]:
            rightx = numx
            righty = numy
            answer += 'R'
            continue

        # gpt
        leftdis = abs(leftx - numx) + abs(lefty - numy)
        rightdis = abs(rightx - numx) + abs(righty - numy)

        if leftdis < rightdis:
            leftx = numx
            lefty = numy
            answer += 'L'
        elif rightdis < leftdis:
            rightx = numx
            righty = numy
            answer += 'R'
        elif rightdis == leftdis:
            if hand == "left":
                leftx = numx
                lefty = numy
                answer += 'L'
            elif hand == 'right':
                rightx = numx
                righty = numy
                answer += 'R'

    return answer