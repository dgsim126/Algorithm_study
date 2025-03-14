def solution(phone_number):

    flag= len(phone_number)-4
    front= flag*"*"
    back= phone_number[flag:]
    answer= front+back
    
    return answer

## main ##
phone_number= "027778888"
print(solution(phone_number))