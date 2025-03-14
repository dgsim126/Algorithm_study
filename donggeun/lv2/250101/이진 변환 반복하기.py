def deleteZero(s):
    cnt= 0
    for i in range(len(s)):
        if(s[i]=="1"):
            cnt+=1

    return str(cnt), str(len(s)-cnt)

def convertTwo(s):
    s= int(s)
    result= ""
    while(s >= 2):
        left= s%2
        s= s//2
        result+=str(left)
    result+=str(s)

    return result

def solution(s):
    cnt= 0
    cnt_0= 0

    while(s!="1"):
        s, how_many= deleteZero(s) # 0을 지운 후, 길이 반환
        s= convertTwo(s) # 해당 길이값을 이진수로 변환
        cnt_0+=int(how_many)
        cnt+=1

    return [cnt, cnt_0]

## main ##
s= "1111111"
print(solution(s))