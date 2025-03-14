def solution(n):
    default_n= n
    n+=1

    while(True):
        if(check(n)==check(default_n)):
            return n
        n+=1

def check(n):
    n= str(format(n, "b")) # format()= google's help

    cnt = 0
    for i in range(len(n)):
        if (n[i] == "1"):
            cnt += 1
    return cnt


## main ##
n= 15
print(solution(n))