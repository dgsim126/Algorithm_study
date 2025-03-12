def solution(n,a,b):
    people = [i for i in range(n)]
    people[a-1] = 'a'
    people[b-1] = 'b'

    round = 1

    while True:
        next = []
        vs = []

        for person in people:
            vs.append(person)

            if len(vs) == 2:
                if 'a' in vs and 'b' in vs:
                    return round

                if 'a' in vs:
                    next.append('a')
                elif 'b' in vs:
                    next.append('b')
                else:
                    next.append(vs[0])
                
                vs = []
            
        people = next
        round += 1