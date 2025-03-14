def solution(n,a,b):
    round= 0

    if(a>b):
        c= a
        a= b
        b= c

    while(True):
        # a, b가 현재 대결하는지 판단
        if(a==b):
            return round

        # a, b가 현재 대결하지 않는다면
        a= (a//2)+(a%2)
        b= (b//2)+(b%2)
        round+=1

## main ##
N= 8
A= 4
B= 7
print(solution(N, A, B))