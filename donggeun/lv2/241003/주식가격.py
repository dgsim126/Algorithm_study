# 이중 for문 쓰는 방법이라 당연히 실패할 줄 알았는데 가볍게 성공(이딴게 level2?)

def solution(prices):
    answer= []

    for i in range(len(prices)-1):
        cnt= 0
        for j in range(i+1, len(prices)):
            if(prices[i]>prices[j]):
                cnt+=1
                answer.append(cnt)
                break
            else:
                cnt+=1
                if(j==len(prices)-1):
                    answer.append(cnt)

    answer.append(0)
    return answer


## main ##
prices= [1, 2, 3, 2, 3]
print(solution(prices))