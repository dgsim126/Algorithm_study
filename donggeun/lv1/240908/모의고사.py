def solution(answers):
    answer= []
    first= [1,2,3,4,5] # 5
    second= [2,1,2,3,2,4,2,5] # 8
    third= [3,3,1,1,2,2,4,4,5,5] # 10
    result= {
        1:0,
        2:0,
        3:0
    }

    for i in range(len(answers)):
        # 0일때, 5일때
        if(first[i%5]==answers[i]):
            result[1]+=1

        # 0일때, 8일때
        if(second[i%8]==answers[i]):
            result[2]+=1

        # 0일때, 10일때
        if(third[i%10]==answers[i]):
            result[3]+=1

    max_= max(result.values()) # google's help(values()를 찾아봄)

    for i in range(3):
        if(max_==result[i+1]):
            answer.append(i+1)

    return answer

## main ##
answers= [1,2,3,4,5]
print(solution(answers))