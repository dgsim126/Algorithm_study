# 현 위치에서 다음 위치로 넘어가며 다음 숫자가 더 크다면 앞에 수 제거
def solution(number, k):
    result = ""
    flag= 0
    current_max= 0
    current_max_index= 0

    number= list(number)
    print(number)
    for i in range(len(number)-1):
        # 탈출조건
        if(flag==k):
            break

        if(int(number[i])>current_max):
            number[current_max_index]= "-1"
            current_max = int(number[i])
            current_max_index= i
            flag+=1
            print(number)
        else:
            if(number[i] < number[i+1]):
                number[i]= "x"
                flag+=1
            print(number)

    print(number)

    for i in range(len(number)):
        if(number[i]!="x"):
            result+=number[i]

    return result


## main ##
number= "4177252841" # "1231234" "4177252841"
k= 4 # 3 4
print(solution(number, k)) # 94 3234 775841