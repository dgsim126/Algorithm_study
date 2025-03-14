def solution(elements):
    len_= len(elements)
    sum_list= set()
    elements= elements+elements

    for length in range(1, len_+1): # 사이즈
        for i in range(len_):
            sum_list.add(sum(elements[i:i+length]))

    return len(sum_list)


## main ##
elements= [7,9,1,1,4]
print(solution(elements))