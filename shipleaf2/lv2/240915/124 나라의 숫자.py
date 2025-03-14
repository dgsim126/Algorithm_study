def solution(n):
    answer = ''
    ternary = int_to_ternary(n)
    ternary_dic = {
        0 : '1',
        1 : '2',
        2 : '4'
    }
    index = 0
    while True:
        if ternary[index] == '1':
            if ternary[index+1] and ternary[index+1] == '0':
                answer = answer + "4"
                index += 2
            elif ternary[index+2]:
                if index + 3 == len(ternary):
                    answer 
                if index + 3 == len(ternary):
                    answer = answer + ternary_dic[index]
                else:
                    answer = answer + "44"
                    index += 3
    return answer

def int_to_ternary(n):
    ternary = ''    
    n = n - 1
    remainder = 0
    while True:
        remainder = n % 3
        ternary = str(remainder) + ternary
        n = n // 3
        if n == 0:
            break
    return ternary

print(int_to_ternary(37))