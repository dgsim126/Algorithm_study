# 투 포인터
def solution(people, limit):
    people.sort()
    boat = 0
    left = 0 # 가장 가벼운 사람
    right = len(people) - 1 # 가장 무거운 사람
    
    while left <= right:
        if people[left] + people[right] <= limit: # 둘 다 태울 수 있으면
            left += 1  # 가벼운 사람 태우고 포인터 이동
        right -= 1 # 무거운 사람은 항상 태우고 포인터 이동
        boat += 1 # 보트 사용 횟수 증가

    return boat

# def solution(people, limit):
#     people.sort()
#     boat = 0

#     while people:
#         total = 0
#         total = people.pop(0)
#         boat += 1
#         if people and people[0] + total <= limit:
#             people.pop(0)
#             boat += 1
#         else:
#             boat += len(people)
#             break
    
#     return boat

# def solution(people, limit):
#     people.sort()
#     boat = 0
#     i = 0

#     while i < len(people):
#         if i == len(people) - 1:
#             boat += 1
#             break

#         if people[i] + people[i + 1] <= limit:
#             boat += 1
#             i += 2
#         else:
#             boat += (len(people) - i)
#             break

#     return boat