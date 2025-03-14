def solution(arr):
    answer = []
    flag= 0
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if(arr[i]!=answer[flag]):
            flag+=1
            answer.append(arr[i])

    return answer

## main ##
arr= [4,4,4,3,3]
print(solution(arr))