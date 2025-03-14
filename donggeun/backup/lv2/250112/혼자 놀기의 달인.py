# gpt

def solution(cards):
    def dfs(start):
        stack = [start]
        visited_group = set()

        while stack:
            current = stack.pop()
            if current not in visited_group:
                visited_group.add(current)
                stack.append(cards[current - 1])  # 다음 상자로 이동

        return visited_group

    visited = set()
    group_sizes = []

    for i in range(1, len(cards) + 1):  # 1번 상자부터 len(cards)번 상자까지
        if i not in visited:
            group = dfs(i)
            group_sizes.append(len(group))
            visited.update(group)

    # 그룹 크기를 내림차순으로 정렬
    group_sizes.sort(reverse=True)

    # 가장 큰 두 그룹의 크기를 곱한 값 반환
    if len(group_sizes) < 2:
        return 0  # 그룹이 하나밖에 없으면 점수는 0
    return group_sizes[0] * group_sizes[1]
