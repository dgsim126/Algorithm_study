# def solution(cards):
#     for i in range(len(cards)):
#         index = [i+1 for i in range(len(cards))]
#         pick1 = 0
#         pick2 = 0
#         max = 0
#         card_box, pick1 = game(cards, i)

        
#         if pick1 * pick2 > max:
#             max = pick1 * pick2

#     return max

# def game(cards, i):
#     card_box = cards
#     start = i
#     next = i
#     pick1 = 0
#     while True:
#         if card_box[start] == 0:
#             break
#         start = card_box[start]
#         card_box[next] = 0
#         next = card_box[start]
#         pick1 += 1

#     return card_box, pick1


def solution(cards):
    def find_group(start, visited):
        group = []
        while start not in visited:
            visited.add(start)
            group.append(start)
            start = cards[start - 1]
        return group

    visited = set()
    groups = []

    for i in range(1, len(cards) + 1):
        if i not in visited:
            group = find_group(i, visited)
            groups.append(len(group))

    if len(groups) < 2:
        return 0

    groups.sort(reverse=True)
    return groups[0] * groups[1]


# 예시 테스트
cards = [8, 6, 3, 7, 2, 5, 1, 4]
print(solution(cards))  # 출력: 12