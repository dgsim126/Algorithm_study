from collections import deque
"""
비슷한 문제가 최근 많이 나왔음
일단 start 순서대로 정렬
하나씩 돌면서 범위 결정
"""

def solution(targets):
    result= 0
    target= deque(sorted(targets))
    print(target) # [[1, 4], [3, 7], [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]]
    left= target[0][0]
    right= target[0][1]
    target.popleft()


    while(target):

        temp= target.popleft()
        new_left= temp[0]
        new_right= temp[1]
        print("current: (", left, right, "), next: (", new_left, new_right, ")")
        print(left, right)

        # 겹치는 경우 : 새로운 값들이 이전 값을 포함할 때, 이전 값이 새로운 값을 포함할 때, 새로운 값의 왼쪽과 이전값의 오른쪽이 겹칠 때
        if(new_left<left and right<new_right):
            print("case 1")
            continue

        elif(left<new_left and new_right<right):
            print("case 2")
            left= new_left
            right= new_right

        elif(new_left<right):
            print("case 3")
            left= new_left

        else:
            print("case 4: result+=1")
            result+=1
            left= new_left
            right= new_right

    return result+1







## main ##
targets= [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))


""" 실행 시 로그 
deque([[1, 4], [3, 7], [4, 5], [4, 8], [5, 12], [10, 14], [11, 13]])
current: ( 1 4 ), next: ( 3 7 )
1 4
case 3
current: ( 3 4 ), next: ( 4 5 )
3 4
case 4: result+=1
current: ( 4 5 ), next: ( 4 8 )
4 5
case 3
current: ( 4 5 ), next: ( 5 12 )
4 5
case 4: result+=1
current: ( 5 12 ), next: ( 10 14 )
5 12
case 3
current: ( 10 12 ), next: ( 11 13 )
10 12
case 3
3
"""