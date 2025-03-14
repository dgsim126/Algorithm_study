def solution(n, words):
    people = [num for num in range(1, n+1)]
    check = []
    last = words[0][0]
    i = 0
    turn = 1

    for word in words:
        if word in check or len(word) == 1 or word[0] != last:
            return [people[i % n], turn]

        check.append(word)
        last = word[-1]

        i += 1
        if i % n == 0:
            turn += 1
        
    return [0,0]