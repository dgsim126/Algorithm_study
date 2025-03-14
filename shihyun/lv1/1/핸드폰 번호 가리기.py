def solution(phone_number):
    star = '*'*(len(phone_number)-4)
    back = phone_number[-4:]
    answer = star+back
    
    return answer