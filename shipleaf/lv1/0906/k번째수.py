def solution(array, commands):
    answer = []
    for i in commands:
        slice_list = array[i[0]-1:i[1]]
        sort_list = sorted(slice_list)
        answer.append(sort_list[i[2]-1])
    return answer


# 테스트
print(solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]]))
