def solution(citations):
    citations.sort(reverse=True)
    h_index = 0

    for i, c in enumerate(citations):
        if c >= i + 1:
            h_index = i + 1
        else:
            break
    
    return h_index


        
print(solution([3, 0, 6, 1, 5]))
print(solution([6,5,5,5,2,1]))
## [6,5,5,5,2,1]