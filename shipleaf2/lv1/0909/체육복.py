# GPT(그리디 개념, 풀이)

def solution(n, lost, reserve):

    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for student in sorted(reserve_set):
        if student - 1 in lost_set:
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)

    return n - len(lost_set)


print(solution(5,[2, 4],[1, 3, 5]))
print(solution(5,[2, 4],[3]))
print(solution(3,[3],[1]))