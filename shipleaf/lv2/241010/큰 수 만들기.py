def solution(number,k):
    def findList(lst):
        n = 0
        for i in range(len(lst)):
            m = number[0:i] + number[i+1:]
            if int(m) > n:
                n = int(m)
            return str(n)

    for i in range(k):
        number = findList(number)

    return number

print(solution("1924",2))
