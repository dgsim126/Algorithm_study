# n*m=yellow(n>=m)가 되는 모든 경우를 찾는다.
# (n*2)+(m*2)+4= brown이 되는 경우를 찾는다.
# return n+2, m+2

def solution(brown, yellow):
    # yellow의 모든 약수를 구한다.
    num= []
    for i in range(1, int(yellow**(1/2))+1):
        if(yellow%i==0):
            num.append(i)
    # print(num)

    len_= len(num)
    for i in range(len_):
        num.append(int(yellow/num[len_-i-1]))
    # print(num)

    # 약수 양 끝단에서 값을 빼면서 조건을 만족하는지 확인
    for i in range(len(num)):
        n= num[len(num)-i-1]
        m= num[i]
        # print(i, n, m)

        # 탈출조건
        if(n < m):
            print("break")
            break

        if((n*2)+(m*2)+4==brown):
            return [n+2, m+2]

## main ##
brown= 24
yellow= 24
print(solution(brown, yellow))