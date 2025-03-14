def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_order = list(skill)
        possible = True

        for sts in skill_tree:
            if sts in skill_order:
                if sts != skill_order[0]:
                    possible = False
                    break
                skill_order.pop(0)
        if possible:
            answer += 1

    return answer