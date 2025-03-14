from collections import deque


def solution(people, limit):
    people = deque(sorted(people, reverse=True))
    count = 0
    print(people)

    while (people):
        if (len(people) < 2):
            count += 1
            return count

        if (people[0] + people[-1] <= limit):
            people.pop()
            people.popleft()
            count += 1
            # print(people)
        else:
            people.popleft()
            count += 1
            # print(people)
    return count

