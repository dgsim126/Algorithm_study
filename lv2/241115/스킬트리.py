def solution(skill, skill_trees):
    cnt= 0

    temp = "BACDE"
    print(temp.index("C"))

    for i in range(len(skill_trees)):
        check= []
        for j in range(len(skill_trees[i])):
            if(skill_trees[i][j] in skill):
                check.append(skill_trees[i][j])
                
        temp= "".join(check) # gpt's help
        if(temp==skill[:len(temp)]): # gpt's help
            cnt+=1

    return cnt


## main ##
skill= "CBD"
skill_trees= ["BACDE", "CBADF", "AECB", "BDA"]
print(solution(skill, skill_trees))