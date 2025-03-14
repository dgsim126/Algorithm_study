def solution(absolutes, signs):
    answer= 0
    for i in range(len(signs)):
        if(signs[i]==True):
            answer+= absolutes[i]
        else:
            answer-= absolutes[i]

    return answer


## main ##
absolutes= [4,7,12]
signs= [True, False, True]
print(solution(absolutes, signs))