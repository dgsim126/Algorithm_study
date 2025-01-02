def solution(s):
    x = s
    count = 0
    num_zero = 0
    while x != "1":
        num_zero += len(x) - x.count("1")
        x = bin(x.count("1")).split("b")[1]
        count += 1
    answer = [count, num_zero]
    return answer