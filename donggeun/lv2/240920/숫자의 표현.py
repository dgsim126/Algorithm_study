def solution(n):
    cnt= 0

    for i in range(1, n+1):
        sum= 0
        temp= i

        while(True):
            # 탈출조건
            if(sum==n):
                cnt+=1
                break
            elif(sum>=n):
                break
            # 반복
            else:
                sum+=temp
                temp+=1

    return cnt

## main ##
n= 15
print(solution(n))