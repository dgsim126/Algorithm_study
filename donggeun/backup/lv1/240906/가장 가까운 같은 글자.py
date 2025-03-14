# 구글 검색을 통해 정수를 아스키코드로 변환하는 함수 이름이 뭔지만 찾음 -> ord()

def solution(s):
    alpa= [-1]*26
    result= []

    for i in range(len(s)):
        flag= ord(s[i])-97

        if(alpa[flag]!=-1):
            result.append(i-alpa[flag])
        else:
            result.append(-1)

        alpa[flag]= i

    return result

## main ##
s= "banana" # s의 길이 <= 10000
print(solution(s))