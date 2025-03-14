def solution(x, y, n):
    answer = 0
    s = set()
    s.add(x)

    while s:
        if y in s:
            return answer

        setx = set()

        for i in s:
            if i + n <= y:
                setx.add(i + n)
            if i * 2 <= y:
                setx.add(i * 2)
            if i * 3 <= y:
                setx.add(i * 3)

        s = setx
        answer += 1

    return -1