from collections import deque

''' 91.7%
def solution(number, k):
    number= list(number)

    current_index= 0
    while(k>0):
        if(current_index<0):
            current_index= 0

        if(current_index>len(number)-2):
            for i in range(k):
                number.pop()
            break

        if(number[current_index] < number[current_index+1]):
            number.pop(current_index)
            current_index-=1
            k-=1
        else:
            current_index+=1

    return "".join(number)
'''


def solution(number, k):
    stack = []

    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    # 아직 k가 남아 있으면 뒤에서 제거
    return ''.join(stack[:len(stack) - k])
