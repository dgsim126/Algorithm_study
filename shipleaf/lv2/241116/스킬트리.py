def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)
        isRight = True

        for s in skill_tree:
            if s in skill_list:
                if s != skill_list[0]:
                    isRight = False
                    break
                skill_list.pop(0)

        if isRight:
            answer += 1

    return answer

# 테스트
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
