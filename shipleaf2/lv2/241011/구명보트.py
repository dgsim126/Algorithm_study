# def solution(people, limit):
#     answer = 0
#     def lifeBoat(lst):
#         for i in range(1, len(lst)):
#             if lst[i] + lst[0] <= limit:
#                 lst.pop(i)
#                 lst.pop(0)
#                 return lst
#         lst.pop(0)
#         return lst
#
#     while people:
#         people = lifeBoat(people)
#         answer += 1
#     return answer

# def solution(people, limit):
#     answer = 0
#     while people:
#         answer += 1
#         boat_with = people.pop(0)
#         for i in range(len(people)):
#             if people[i] + boat_with <= limit:
#                 people.pop(i)
#                 break
#     return answer

# GPT

def solution(people, limit):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats

print(solution([70, 50, 80, 50], 100))

print(solution([70,50,80,50], 100))
# print(solution([70,80,50], 100))
# print(solution([100, 200, 150, 50, 60], 210))
# print(solution([100, 100, 100, 100], 200))
# print(solution([90,90,90,90], 100))
# print(solution([40, 50, 150, 160], 200))
# print(solution( [40, 40, 40, 40, 40], 80))
# print(solution([120, 121, 122, 123, 124], 125))
# print(solution([40, 200, 40, 200, 40], 240))
print(solution([60, 61, 62, 63, 64], 120))