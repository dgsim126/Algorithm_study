# GPT

def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            max_divisor = 1
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    if i // j <= 10**7:
                        max_divisor = max(max_divisor, i // j)
                    else:
                        max_divisor = max(max_divisor, j)
            answer.append(max_divisor)
    
    return answer
