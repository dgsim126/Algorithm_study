# people를 정렬한 후, 각 리스트 양 끝단에서 값을 뺀다.
from collections import deque

def solution(people, limit):
    people= sorted(people, reverse=True)
    cnt= 0
    people= deque(people)
    # print(people)

    while(len(people)):
        if(len(people)==1): # 안 탄 사람이 1명인 경우
            cnt+=1
            break

        max_= people.popleft()
        min_= people[-1]

        if(max_+min_>limit): # 혼자 타야하는 경우
            cnt+=1
            continue
        else: # 둘이 탈 수 있는 경우
            people.pop()
            cnt+=1
            continue
    return cnt



## main ##
people= [70, 50, 80, 50]
limit= 100
print(solution(people, limit))