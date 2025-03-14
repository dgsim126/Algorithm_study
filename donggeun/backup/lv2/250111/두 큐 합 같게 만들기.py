"""
두 큐의 합을 구한 후 반으로 나눠 각 큐가 가져야 하는 사이즈 저장
> 두 개의 방향이 있는데 두 방향 중 하나를 미리 판단 가능한가? -> 각 방향으로의 함수 2개 만들어서 결과 리턴 후 비교
circular queue?

"""
def check(half, queue):
    queue.append(-1)
    start= 0 # 0
    end= (len(queue)//2) # 4
    cnt= 0

    while(queue[start]!=-1 and queue[end]!=-1):
        if(sum(queue[start:end])==half):
            # print(queue[start:end])
            return cnt
        elif(sum(queue[start:end])<half):
            end+=1
        else:
            start+=1
        cnt+=2

    # print(queue[start:end])
    return cnt

def solution(queue1, queue2):
    half= (sum(queue1)+sum(queue2))//2 # 15
    queue= queue1+queue2 # [3, 2, 7, 2, 4, 6, 5, 1]
    queue_reverse= queue2[::-1]+queue1[::-1] # [1, 5, 6, 4, 2, 7, 2, 3]

    num1= check(half, queue)
    num2= check(half, queue_reverse)
    # print(num1, num2)

    return min(num1, num2)





## main ##
queue1= [3, 2, 7, 2]
queue2= [4, 6, 5, 1]
print(solution(queue1, queue2))