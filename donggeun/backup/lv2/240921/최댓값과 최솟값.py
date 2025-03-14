def solution(s):
    numbers= list(map(int, s.split())) # gpt's help

    min_= min(numbers)
    max_= max(numbers)

    return f"{min_} {max_}"


## main ##
s = "-1 -1"
print(solution(s))
