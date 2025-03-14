def solution(participant, completion):
    sorted_part = sorted(participant)
    sorted_comp = sorted(completion)

    sorted_comp.append(0)

    for i in range(len(sorted_part)):
        if sorted_part[i] != sorted_comp[i]:
            return sorted_part[i]
        
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))