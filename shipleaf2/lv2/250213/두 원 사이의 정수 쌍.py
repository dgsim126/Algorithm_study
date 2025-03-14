# def solution(r1, r2):
#     sum_r2 = 4 * r2 + 1                                                     
#     if (2*(r2-1)**2)**(1/2) < r2:
#         sum_r2 += 4*(r2-1)**2
#     else:
#         sum_r2 += 4*(r2-1)**2 - 1

#     sum_r1 = 4 * (r1-1) + 1

#     if (2*(r1-1)**2)**(1/2) < r1:
#         sum_r1 += 4*(r1-1)**2
#     else:
#         sum_r1 += 4*(r1-1)**2 - 1

#     return sum_r2 - sum_r1

import math

def solution(r1, r2):
    answer = 0
    for i in range(1, r2+1):
        if i < r1 :
            s = math.ceil(math.sqrt((r1**2 - i**2)))
        else : 
            s = 0

        e = int(math.sqrt((r2**2 - i**2)))
        answer = answer + e - s + 1

    return answer*4