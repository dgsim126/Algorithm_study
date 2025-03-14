

def compression(s, size):
    # 맨 앞에서 size 만큼을 꺼내서 해당 값(default)을 이용해 뒤에 값과 같은지 비교
    # 같은 값이 몇 번 반복되는지 확인하고 다른 값이 나오면 반복 중단
    ## 같은 값이 한 번도 안 나왔다면 s=s[1:] 하고, result에 default를 추가)
    ## 같은 값이 여러번 나왔다면 result에 default를 넣고 반복된 숫자 넣기



def solution(s):
    # 압축 글자 단위를 s의 절반 사이즈만큼 검사하며, 최소 길이를 구하라

    min_len= 1000

    for i in range(1, len(s)//2):
        temp= compression(s, i)
        print(temp)
        if(temp < min_len):
            min_len= temp

    return min_len



## main ##
s= "aabbaccc"
print(solution(s))